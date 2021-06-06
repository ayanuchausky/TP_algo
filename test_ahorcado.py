"""

Parte hecha por Agustín Esteban Conti - Etapa 1
Esta parte del codigo es la estructura principal
del juego.

"""
"""palabra_a_adivinar = "auto" #palabra usada para testear"""

def palabra_insertada_a_interrogacion(palabra_a_adivinar, letras_usadas):
#     Agustín Conti: Crea una cadena de interrogaciones igual de larga que la palabra
    interrogaciones=""
    for caracter in palabra_a_adivinar:
        if letras_usadas.count(caracter) != 0:
            interrogaciones += caracter
        else: 
            interrogaciones += "?"
    return interrogaciones

def victoria(letras_usadas, palabraParaJuego):
#     Agustín Conti: Si todas las letras fueron adivinadas regresa un True
    ganar = False
    if palabra_insertada_a_interrogacion(palabraParaJuego, letras_usadas).count("?") == 0:
        ganar = True
    return ganar

def contar_aciertos(letra_ingresada, palabraParaJuego):
#     Agustín Conti: Suma un acierto si la letra ingresada esta en la palabra a adivinar
    aciertos=0
    if palabraParaJuego.count(letra_ingresada)!=0:
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

def ejecutarJuego(palabraParaJuego):
    #     Ejecuta el juego
    letras_usadas=[]
    aciertos=0
    desaciertos=0
    CANTIDAD_DESACIERTOS_PERDER= 8
    letra_ingresada=""
    letras_derrota=""
    print("Palabra a adivinar:",palabra_insertada_a_interrogacion(palabraParaJuego, letras_usadas), "Aciertos:",aciertos , "Desaciertos:",desaciertos, letras_derrota)
    while desaciertos < CANTIDAD_DESACIERTOS_PERDER and not victoria(letras_usadas, palabraParaJuego) and letra_ingresada != "fin" and letra_ingresada!="0":
        letra_ingresada=ingrese_letra(letras_usadas)
        if letra_ingresada!="fin" and letra_ingresada!="0":
            if contar_aciertos(letra_ingresada, palabraParaJuego) > 0:
                aciertos += contar_aciertos(letra_ingresada, palabraParaJuego)
                print_interfaz(palabraParaJuego, aciertos, desaciertos, "Muy bien!!!", letras_derrota, letras_usadas)
            else:
                desaciertos += 1
                letras_derrota += " " + letra_ingresada
                print_interfaz(palabraParaJuego, aciertos, desaciertos, "Lo siento!!!", letras_derrota, letras_usadas)
    if not desaciertos<CANTIDAD_DESACIERTOS_PERDER:
        print("Has perdido")
    elif victoria(letras_usadas, palabraParaJuego):
        print("Has ganado")
    else:
        print("Game over")

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

"""ETAPA 3"""
import random

def define_word_list(dictionary):
    pre_candidatas = []
    for key in dictionary:
        pre_candidatas += key
    return pre_candidatas


"""ver como se comporta esta funcion cuando el usuario simplementer retorna enter; toma el -1 por default correctamente?"""
def longitud_deseada():
    ingresar_long = int(input("Ingrese la longitud deseada para la palabra: "))
    return ingresar_long

def filtrar_palabras(lista_de_palabras,longitud):
    palabras_candidatas = []
    palabras_no_candidatas = 0
    if(longitud == -1):
        palabras_candidatas = lista_de_palabras
    else:
        for palabra in lista_de_palabras:
            """Creo que esta parte esta mal porque se trabaja con el input de la funcion como si fuera una lista en vez de un diccionario"""
            if len(palabra) == longitud:
                palabras_candidatas += [palabra]
            elif len(palabra) != longitud:
                palabras_no_candidatas += 1
    if palabras_no_candidatas == len(lista_de_palabras):
        ingresar_nueva_longitud = int(input("No hay palabras la longitud deseada en el texto. Ingrese otra longitud: "))
        palabras_candidatas = filtrar_palabras(lista_de_palabras,ingresar_nueva_longitud)
    return palabras_candidatas

def random_word(lista_de_candidatas):
    palabra_elegida = lista_de_candidatas[random.randint(0,len(lista_de_candidatas) - 1)]
    return palabra_elegida

def obtenerPalabra(diccionarioDePalabras, longitudDeseada = -1):
    """longitud = longitud_deseada()"""
    """lista_de_palabras = ["hola", "como", "estas", "estamos", "haciendo", "un", "TP"]"""
    longitud = longitudDeseada
    lista_de_palabras = diccionarioDePalabras
    palabras_filtradas = filtrar_palabras(lista_de_palabras,longitud)
    palabra_elegida = random_word(palabras_filtradas)
    return palabra_elegida

def main():
    palabraParaJuego = obtenerPalabra(palabras_candidatas(), longitud_deseada())
    ejecutarJuego(palabraParaJuego)

main()
