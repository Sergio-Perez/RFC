from src import comprobarImagen
from src import capturarImagen

from flask import request
from api.app import *
from api.config import PORT
import api.controllers.params
import api.controllers.analizarfoto 
import api.controllers.cargarImagen







app.run("0.0.0.0", PORT, debug=True)



