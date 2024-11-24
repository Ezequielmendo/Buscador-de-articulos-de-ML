from flask import Flask, render_template, request, jsonify
from bs4 import BeautifulSoup
import requests

def create_app():
    app = Flask(__name__)
    app.secret_key = '_secret.key_'

    @app.route('/', methods=['GET','POST'])
    def buscar():
        is_searching = False
        if request.method == 'POST':
            is_searching = True
            producto = request.form['articulo']
            url = f"https://listado.mercadolibre.com.ar/{producto}"
            response = requests.get(url)
            
            if response.status_code != 200:
                return jsonify({"error": "No se pudo acceder a la página"})
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Buscar el total de publicaciones
            total_publicaciones = soup.find('span', {'class': 'ui-search-search-result__quantity-results'})
            if total_publicaciones:
                total = int(total_publicaciones.text.split()[0].replace('.', ''))
            
                # Definir criterio de recomendación
                if total > 70000:
                    recomendacion = "Alta competencia. No se recomienda vender este producto."
                elif total > 30000:
                    recomendacion = "Competencia moderada. Considera venderlo con un enfoque único."
                else:
                    recomendacion = "Buena oportunidad. Poca competencia en el mercado."
                return jsonify({"total": total, "recomendacion": recomendacion})
            else:
                return jsonify({"error": "No se encontraron resultados"})

        elif request.method == 'GET':
            return render_template('index.html', is_searching=False)
        return render_template('index.html', is_searching=is_searching)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0',port=5000)