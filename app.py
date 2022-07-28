#Crearemos un rest api para obtener los 2 colores principales desde la url de una imagen de spotify: https://i.scdn.co/image/ab67616d0000b27334362676667a4322838ccc97
#Para ello usaremos la libreria de python flask

#librerias
from flask import Flask, request, jsonify
import requests
from io import BytesIO
from PIL import Image
from colorthief import ColorThief

#creamos la app
app = Flask(__name__)

#creamos la ruta
@app.route('/', methods=['GET'])
def get_colors():
    #obtenemos la url de la imagen
    url = request.args.get('url')
    #Guardamos la imagen en la carpeta raiz
    response = requests.get(url)

    with open('image.png', 'wb') as f:
        f.write(response.content)
    #Obtenemos los colores de la imagen
    
    color_thief = ColorThief('image.png')

    #obtenemos los 2 colores principales
    dominant_color = color_thief.get_color(quality=1)
    palette = color_thief.get_palette(color_count=2)
    #creamos un diccionario con los colores
    colors = {
        'dominant_color': dominant_color,
        'palette': palette
    }
    #retornamos los colores en formato json
    return jsonify(colors)

#ejecutamos la app
if __name__ == '__main__':
    app.run(debug=True)