# Buscador de Artículos en MercadoLibre

Este proyecto es una aplicación web desarrollada con **Flask**, que permite buscar artículos en MercadoLibre y mostrar recomendaciones sobre la competencia basada en la cantidad de resultados obtenidos.

## Descripción

La aplicación toma como entrada un término de búsqueda, busca los productos relacionados en MercadoLibre y muestra la cantidad de artículos encontrados. Luego, proporciona una recomendación sobre si es conveniente vender ese producto, dependiendo de la cantidad de competencia (número de publicaciones).

## Características

- Búsqueda en MercadoLibre usando **BeautifulSoup** para parsear la información.
- Muestra la cantidad de artículos encontrados y da recomendaciones según la competencia.
- Interfaz web simple y fácil de usar.

## Tecnologías utilizadas

- **Flask**: Framework de desarrollo web en Python.
- **BeautifulSoup**: Librería de Python para parsear HTML y obtener información de páginas web.
- **Requests**: Librería para hacer peticiones HTTP.
- **HTML/CSS**: Para la estructura y el diseño de la interfaz web.

## Instalación

Para instalar y ejecutar este proyecto en tu máquina local, sigue estos pasos:

1. Clona el repositorio en tu máquina:
git clone https://github.com/tu-usuario/buscador-mercadolibre.git

2. Entra en el directorio del proyecto:
cd buscador-mercadolibre

3. Crea un entorno virtual (opcional pero recomendado):
python -m venv venv

4. Activa el entorno virtual:
- En Windows:
  ```
  venv\Scripts\activate
  ```
- En macOS/Linux:
  ```
  source venv/bin/activate
  ```

5. Instala las dependencias:
pip install -r requirements.txt

