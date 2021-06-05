"""
Parte hecha por Juan Ignacio D`Angona - Etapa 2
Esta parte del codigo se encarga de clasificar
las palabras del texto dado, acorde a las condiciones
impuestas por la consigna.

"""
from texto import obtener_texto

def palabras_candidatas():
    texto_a_procesar=str(obtener_texto())
    texto_procesado=((texto_a_procesar.casefold()).replace(".","")).split() #Esta funcion es para separar cada palabra del texto
    diccionario_palabras={}
    contador_palabras_diccionario=0 
    for palabra in texto_procesado:                  
        if (palabra.isalpha()) and len(palabra)>=5:  #Son las condiciones para que la palabra sea aceptada
            if palabra not in diccionario_palabras:
                diccionario_palabras[palabra]=1
            else:
                diccionario_palabras[palabra]+=1           
    lista_palabras =sorted(diccionario_palabras.items())
    for elemento in lista_palabras: 
        contador_palabras_diccionario+=1
        print(elemento)
    print("Palabras distintas en total:", contador_palabras_diccionario)
    return diccionario_palabras

"""

Parte hecha por Agustín Esteban Conti - Etapa 1
Esta parte del codigo es la estructura principal
del juego.

"""
palabra_a_adivinar = "auto" #palabra usada para testear

def palabra_insertada_a_interrogacion(palabra_a_adivinar, letras_usadas):
#     Agustín Conti: Crea una cadena de interrogaciones igual de larga que la palabra
    interrogaciones=""
    for caracter in palabra_a_adivinar:
        if letras_usadas.count(caracter) != 0:
            interrogaciones += caracter
        else: 
            interrogaciones += "?"
    return interrogaciones

def victoria(letras_usadas):
#     Agustín Conti: Si todas las letras fueron adivinadas regresa un True
    ganar=False
    if palabra_insertada_a_interrogacion(palabra_a_adivinar,letras_usadas).count("?")==0:
        ganar=True
    return ganar

def contar_aciertos(letra_ingresada):
#     Agustín Conti: Suma un acierto si la letra ingresada esta en la palabra a adivinar
    aciertos=0
    if palabra_a_adivinar.count(letra_ingresada)!=0:
        aciertos+=1
    return aciertos

def print_interfaz(palabra_a_adivinar, aciertos, desaciertos,mensaje,letra_derrota,letras_usadas):
#     Agustín Conti: Imprime la interfaz del juego
    if desaciertos==0:
        print(mensaje,palabra_insertada_a_interrogacion(palabra_a_adivinar,letras_usadas), "Aciertos:",aciertos , "Desaciertos:",desaciertos)
    else:
        print(mensaje,palabra_insertada_a_interrogacion(palabra_a_adivinar,letras_usadas), "Aciertos:",aciertos , "Desaciertos:",desaciertos,"-",letra_derrota) 

def ingrese_letra(letras_usadas):
#     Agustín Conti: Pide al usuario que ingrese una letra y verifica que sea apropiada
    letra_ingresada=str(input("Ingrese letra: ")).casefold()
    if letra_ingresada!="0" and letra_ingresada!= "fin":
        while (not letra_ingresada.isalpha() or len(letra_ingresada)!=1 or letras_usadas.count(letra_ingresada) != 0):
            if  letras_usadas.count(letra_ingresada) != 0:
                print (letra_ingresada, "ya fue ingresada")
            else:
                print ("Ingreso inválido")
            letra_ingresada=str(input("Ingrese letra: ")).casefold()
    letras_usadas.append(letra_ingresada)
    return letra_ingresada

def main():
#     Ejecuta el juego
    letras_usadas=[]
    aciertos=0
    desaciertos=0
    CANTIDAD_DESACIERTOS_PERDER= 8
    letra_ingresada=""
    letras_derrota=""
    print("Palabra a adivinar:",palabra_insertada_a_interrogacion(palabra_a_adivinar, letras_usadas), "Aciertos:",aciertos , "Desaciertos:",desaciertos, letras_derrota)
    while desaciertos<CANTIDAD_DESACIERTOS_PERDER and not victoria(letras_usadas) and letra_ingresada!="fin" and letra_ingresada!="0":
        letra_ingresada=ingrese_letra(letras_usadas)
        if letra_ingresada!="fin" and letra_ingresada!="0":
            if contar_aciertos(letra_ingresada)>0:
                aciertos+=contar_aciertos(letra_ingresada)
                print_interfaz(palabra_a_adivinar, aciertos, desaciertos,"Muy bien!!!",letras_derrota,letras_usadas)
            else:
                desaciertos+=1
                letras_derrota+=" "+letra_ingresada
                print_interfaz(palabra_a_adivinar, aciertos, desaciertos,"Lo siento!!!",letras_derrota,letras_usadas)
    if not desaciertos<CANTIDAD_DESACIERTOS_PERDER:
        print("Has perdido")
    elif victoria(letras_usadas):
        print("Has ganado")
    else:
        print("Game over")
    letras_usadas=[]