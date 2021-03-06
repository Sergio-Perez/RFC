
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import glob
import os
import numpy as np


def descargarDataset(path2):
    imagenes_fruta = []
    clase = [] 
    for directorio in glob.glob(path2):
        nombre = directorio.split("/")[-1]
        for imagen_archivo in glob.glob(os.path.join(directorio, "*.*g")):
            imagen = cv2.imread(imagen_archivo, cv2.IMREAD_COLOR)
        
            imagen = cv2.resize(imagen, (35,35))
            imagen = cv2.cvtColor(imagen, cv2.COLOR_RGB2BGR)
        
            imagenes_fruta.append(imagen)
            clase.append(nombre)
    imagenes_fruta = np.array(imagenes_fruta)
    clase = np.array(clase)
    return clase ,imagenes_fruta 





def descargarDataset_FFT(path2):
    imagenes_fruta = []
    clase = [] 
    for directorio in glob.glob(path2):
        nombre = directorio.split("/")[-1]
        for imagen_archivo in glob.glob(os.path.join(directorio, "*.*g")):
            imagen = cv2.imread(imagen_archivo, 0)
            dft = cv2.dft(np.float32(imagen),flags = cv2.DFT_COMPLEX_OUTPUT)
            dft_shift = np.fft.fftshift(dft)
            
        
            imagenes_fruta.append(dft_shift)
            clase.append(nombre)
    imagenes_fruta = np.array(imagenes_fruta)
    clase = np.array(clase)
    return clase ,imagenes_fruta 