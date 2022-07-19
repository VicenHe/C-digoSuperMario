import cv2 as cv
import numpy as np
import os
from time import time
from Prueba import fram
from windowcapture import WindowCapture
from Vns import Vns
from PIL import Image
from hsvfilter import HsvFilter
import pyautogui
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Key2.json"

#Función de Google para extraer texto de una imagen
def detect_text(path):
    from google.cloud import vision
    import io
    #Se crea el objeto cliente
    client = vision.ImageAnnotatorClient()
    #Se lee la imagen
    with io.open(path, 'rb') as image_file:
        content = image_file.read()
        #Se crean los bytes de la imagen
    image = vision.Image(content=content)
    #Se obtienen coordenadas de la imagen
    response = client.text_detection(image=image)
    texts = response.text_annotations
    description=[]
    i=0
    for text in texts:
        if i>0:
            description.append(text.description)
        i=i+1
        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])
    #Se retornan los datos en el string description
    return description

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

wincap = WindowCapture('Mesen - Super Mario Bros. (World)')
vision_limestone = Vns('X.jpg')
#vision_limestone.init_control_gui()

#Variables para la lógica
loop_time = time()
Time=False
ind=0
description2=[]
ttm=10
ttm2=100
while(True):
    #Se obtienen los screenshot
    screenshot = wincap.get_screenshot()
    #Filtro para mejorar resultados
    hsv_filter = HsvFilter(0, 0, 0, 179, 255, 255, 0, 0, 0, 0)
    #Imagen con el filtro añadido
    processed_image = vision_limestone.apply_hsv_filter(screenshot, hsv_filter)
    rectangles = vision_limestone.find(processed_image, 0.55)
    detection_image = vision_limestone.draw_rectangles(screenshot,rectangles)

    #screenshot.save("converted.png", format="png")
    #Se guarda un frame en forma de imagen
    cv.imwrite("converted.png",processed_image)
    description=[]
    #Se extrae el texto del frame obtenido
    description=detect_text("converted.png")
    print("description", description)
    
    print("description output",description)
    #Si se obtiene texto se intenta
    if len(description)>0:
        try:
        #Si está TIME en la descripción sigue el código
           ind= description.index('TIME')
           print("description",description)
        #El elemento que sigue después de TIME es el nivel, por ejemplo, 1-2
           p=str(description[ind+1].replace("'","").replace(":",""))
           x=int(p)
           description2=description
           ttm=1
        #Cuando TTM= 1 significa que se encuentra TIME en la selección de la descripción
        #Se cambia su valor a 10 para reiniciar el loop de detección

        except Exception as e: 
            print(e)

            if ttm==1:
                if '-' in description2[ind+1]:
                    fr= fram(description2[ind-2])
                    ttm=10
                    ttm2=100
                else:
                    val='1-1'
                    for x in description2:
                                if '-' in x:
                                    val=x
                            #Se reemplaza el valor de lo encontrado después de TIME
                            # Que sería el nivel para mostrar un gif del nivel específico
                            # Y se reinician los valores
                    fr= fram(val)
                    ttm=10
                    ttm2=100

        try:
            #Se crea otro TRY por la variable ttm2, a veces OCR detecta números en otra parte de la descripción
            # por lo tanto, se crea esta nueva variable
                ind= description.index('TIME')
                print("description2",description)
                s=str(description[ind+2].replace("'","").replace(":",""))
                x=int(s)
                description2=description
                ttm2=11


        except Exception as e: 
                    print(e)
                    if ttm2==11:
                        if '-' in description2[ind+1]:
                            fr= fram(description2[ind+1])
                            ttm2=100
                            ttm=10
                        else:
                            val='1-1'
                            for x in description2:
                                if '-' in x:
                                    val=x
                            fr= fram(val)
                            ttm2=100
                            ttm=10

# Se crea la posibilidad de obtener el GAME OVER en el juego, para reemplazar con el gif donde se murió
        if 'OVER' in description:
                        val=""
                        for x in description2:
                                if '-' in x:
                                    val=x
                                else:
                                    val='1-1'
                        fr= fram(val)
                        ttm2=100
                        ttm=10


    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Completado.')