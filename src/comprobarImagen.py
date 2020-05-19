def comprobarImagen(path):
  
    imagen = cv2.imread(path, cv2.IMREAD_COLOR)#cargo la imagen
    new_model = load_model('./Input/modelos/path_to_my_modelPrimero3Parte.h5' ,custom_objects=None,compile=False)#cargo el modelo  estudiado
   
    imagenes = cv2.resize(imagen, (35,35))# Reduzco la imagena 35x35
    imagenes = cv2.cvtColor(imagenes, cv2.COLOR_RGB2BGR)
    image = np.expand_dims(imagenes, axis=0)# Expando la imagen
    image = imagenes.reshape(1,35*35*3)# Redimensiono la imagen

    ynew = new_model.predict_classes(image)   
    nombre_frutas = pd.read_csv("./Input/nombre_Frutas.csv")
    translator = Translator()
    nombre=""    
    for i in range(len(image)):
        ynew[i]
        for indice, value in nombre_frutas.items():    
        
            if value[0] == ynew[i]:
                nombre += indice
    
    result = translator.translate(nombre,src ='en',dest='es')
    plt.xlabel(result)  
    myobj = gTTS(text=result.text, lang='es', slow=False) 
    myobj.save("./Input/fruta.mp3") 
    mixer.init()
    mixer.music.load('./Input/fruta.mp3')
    mixer.music.play()
    plt.imshow(imagen)
    plt.xlabel(result.text)