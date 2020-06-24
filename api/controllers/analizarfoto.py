from api.app import app
from ..helpers.errorHandler import *
from src import capturarImagen
import cv2
from src import comprobarImagen
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from api.config import pathImagen
from flask import render_template_string




#def analizarfoto():
    
@app.route("/comprobar")
@errorHandler   
def capturarImagen():
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Webcam para Frutas")
    img_counter = 0

    while True:
        ret, frame = cam.read()

        if not ret:
            print("Fallo al  grabar imagen")
            cv2.destroyAllWindows()
            return """<img src ="https://image.freepik.com/vector-gratis/nino-buscando-linterna_7710-126.jpg" />
            <h1>Fallo al sacar camaraweb</h1>"""
            break
        cv2.imshow("Webcam para Frutas", frame)
        k = cv2.waitKey(1)

        if k%256 == 27:
            # Presionar ESC 
            print("Pulsar Escape , cerrando...")
            cv2.destroyAllWindows()
            
            break
        elif k%256 == 32:
            # Presionar SPACE 
            img_name = "./static/img/opencv_frame_{}.jpg".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1
            cv2.destroyAllWindows()
            
            
        if img_name == None:
          raise APIError("Fallo al  grabar imagen") #"""<img src ="https://image.freepik.com/vector-gratis/nino-buscando-linterna_7710-126.jpg" />"""
        else :
          img_name = "./static/img/opencv_frame_0.jpg"
             
          comprobarImagen.comprobarImagen(img_name)
          return   """  <img src="/static/img/opencv_frame_0.jpg" />
          <h1>Fruta</h1>"""




@app.route("/")
@errorHandler
def fotoInicio():
     return render_template_string(open("api/controllers/template/pagina-inicio.html",'r').read())
    


@app.route("/comprobar/imagen-guardada")
@errorHandler
def analizarImagen():
 
  try:
    comprobarImagen.comprobarImagen(pathImagen)
    return """
  <img src="/static/img/fruta.jpg" />
  <h1>  Fruta </h1>
  """
  except:
    raise APIError("Fallo el sonido")
  