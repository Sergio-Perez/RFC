![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Proyecto RFC (Reconocimiento de Frutas para Ciegos) 🍎🍌🍓🍍🥥

![Frutas](https://4.bp.blogspot.com/-P_Lw3bNsXfo/Vt3GJ4t6WGI/AAAAAAAAPv4/n5Kx0eUjz8Y/s1600/20160307_095029_resized.jpg)

## Descripción:

En este proyecto vamos a tratar de analizar un dataset descargado de Kaggle("frutas360"),limpiarlo ,analizarlo y pasarle una red neuronal. Después de tener un modelo que predice captar un aimagen desde una webcam, analizarla y hacer que el ordenador por el sonido diga que fruta cree que es. Para desplegarlo crearemos una Api.

### Limpieza:

En la limpieza del datase empezamos descargando los archivos, primero los de train y despues los de set. Sacamos el nombre de las carpetas como el nombre de cada fruta. Ya esos nombres los pasamos a categoricos, es decir le damos valores númericos.

### Análisis de datos:

Vemos el tipoo de datos hacemos unas imágenes para ver sus distancias despúes de hacerles una estandarización y reducir sus dimensiones a dos con un [PCA](https://es.wikipedia.org/wiki/An%C3%A1lisis_de_componentes_principales), y hacerles un [T-SNE](https://en.wikipedia.org/wiki/T-distributed_stochastic_neighbor_embedding)


## Empezamos con el ["Machine Learning"](https://es.wikipedia.org/wiki/Aprendizaje_autom%C3%A1tico)

Empezamos haciendo pruebas con Random Forest Clasification, en las cuales nos sale unos valores no muy buenos. También probamos pasandole el PCA, y el "acurracy" tampoco mejora.
Probamos varios modelos más con algunos sacando muy buenos resultados. Como con el SVM Linear con un "acurracy" muy alto.

Como nuestro proposito era meterle una red neuronal nos encaminamos  a ello y con el módulo Keras hacemos la predición usando tensorflow.
Tenemos  un "acurracy" muy alto. Pero a la hora de las pruebas reales fuera de nuestro dataset de test el anierto es muy bajo.
Viendo esto buscamos soluciones y tomamos estas:
        ----> Primero: Cojemos más muestras y se las añadimos al dataset. Pero con 107 clases no mejoro mucho
        ----> Segundo: Agrupamos muestras y reducimos el numero de clases a 63. Pero tampoco encontramos una mejora
        ----> Tercero: Reducimos las muestras a 5 y elejimos frutas muy dispares entre ellas.

## Primero:

Al tomar este camino tuvimos un problema de manejo de datos por su gran volumen más de 5 gigas de tamaño total. Lo solucionamos subiendo a google Drive las muestras y usando google Colab y su GPU para procesar los datos con mayor celeridad.

### Segundo:

Cuando tomamos este camino usamos la misma tecnica para procesar los datos.
Hicimos una matriz de confusion para analizar los datos y ver que eran buenos un alto "[acurracy](https://es.wikipedia.org/wiki/Precisi%C3%B3n_y_exactitud)".
Pero le pasaba lo mismo a la hora de pasarle una foto desde una webcam.

### Tercero:

En este tercer camino reducimos a 5 clases (Piñas, Manazas, Cocos, Platanos y Fresas). En este caso opté por hacer un cambio en la manera de manejar los datos tratandolos con la FFT([Transformada de fourier](https://es.wikipedia.org/wiki/Transformada_de_Fourier)).
En este caso el modelo  también dio un "acurracy" muy bajo por eso este no lo tuve en cuenta.


# API:

Ya montados todas las funciones que use en .py, fui a montar la Api usando la libreria Flask.

### Su uso:

    ---> /carga-imagen:  Puedes subir una imagen desde tu disco duro.
    ---> /comprobar   :  Hace una foto y  analiza que fruta has sacado por ella. 
    ---> /comprobar/imagen-guardada:  Comprueba la imagen que has subido desde "/cargar-imagen"


