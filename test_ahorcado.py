def palabra_insertada_a_interrogacion(palabra_a_adivinar):
    #Agustín Conti: convierte la palabra en "?"
    interrogaciones=""
    for i in range(0,len(palabra_a_adivinar)):
        interrogaciones+="?"
    return interrogaciones

#asdz

def interfaz(palabra_a_adivinar):
    #Agustín Conti: Imprime la interfaz del juego, faltan muchas cosas
    aciertos=0
    desaciertos=0
    print("Palabra a adivinar:",palabra_insertada_a_interrogacion(palabra_a_adivinar), "Aciertos: ",aciertos , "Desaciertos: ",desaciertos)
