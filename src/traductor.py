import goslate

text = nombre_frutas_corregido[0]
gs = goslate.Goslate()
translatedText = gs.translate(text,'es')


def traductor(lista):#translate
    translator = Translator()
    espanol=[]
    for e in lista:
        print(e)
        traduciendo = translator.translate(e, src='en',dest='es')
    
        espanol.append(traduciendo.text)
    return    espanol
#probando = traductor(np.unique(nombre_frutas_corregido))
