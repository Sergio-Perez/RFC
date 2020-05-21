from api.app import app
from api.config import UPLOAD_FOLDER
from flask import request, redirect
from werkzeug.utils import secure_filename
import os
from flask import render_template_string
import sys
from ..helpers.errorHandler import *


sys.path.append("/api/controllers")

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF"]
app.config["MAX_IMAGE_FILESIZE"] = 0.5 * 4024 * 3024

def allowed_image(filename):
    if not "." in filename:
        return False
    ext = filename.rsplit(".", 1)[1]
    print(filename)
    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        
        return True
    else:
        return False

def allowed_image_filesize(filesize):
    if int(filesize) <= app.config["MAX_IMAGE_FILESIZE"]:
        return True
    else:
        return False

@app.route("/cargar-imagen", methods=["GET", "POST"])
@errorHandler
def upload_image():
    if request.method == "POST":
        
        if request.files:
           
           # if "filesize" in request.cookies:
           #     print("hola",request.files)
            #    if not allowed_image_filesize(request.cookies["filesize"]):
            #        print("Tamaño de archivo es excesivo")
            #        return redirect(request.url)
                # request.form.getlist('name[]')
            
            image = request.files["image"]
            print("imagen",image,"hola",image.filename)
            if image.filename == "":
                print("Hola Archivo no encontrado")
                return redirect(request.url)

            if allowed_image(image.filename):
                filename = "fruta.jpg"
                        
                image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                print("Imagen grabada")
                return redirect(request.url)

            else:
                print("El nombre de la extension del archivo no es valido")
                return redirect(request.url)

    return render_template_string(open("api/controllers/template/upload_imagen.html",'r').read())
