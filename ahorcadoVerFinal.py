"""

Parte hecha por Agustín Esteban Conti - Etapa 1
Esta parte del codigo es la estructura principal
del juego.

"""

from os import system

def cadenaInterrogacion(palabra_a_adivinar, letras_usadas):
#     Agustín Conti: Crea una cadena de interrogaciones igual de larga que la palabra
    interrogaciones=""
    for caracter in palabra_a_adivinar:
        if letras_usadas.count(caracter) != 0:
            interrogaciones += caracter
        else: 
            interrogaciones += "?"
    return interrogaciones

def victoria(letras_usadas, palabra_a_adivinar):
#     Agustín Conti: Si todas las letras fueron adivinadas regresa un True
    ganar=False
    if cadenaInterrogacion(palabra_a_adivinar,letras_usadas).count("?")==0:
        ganar=True
    return ganar

def preguntarNuevoJuego():
    """
    Consulta al jugador si desea continuar jugando al videojuego.
    [Hecha por: Micael Virgilio]
    """
    print("")
    nuevoJuego = False
    seguir = input("¿ Desea adivinar otra palabra ? [Ingrese \"SI\"/\"NO\"]: ").upper()
    while seguir != "SI" and seguir !="NO":
        print("Ingreso inválido. Por favor, ingrese [\"SI\"/\"NO\"].")
        seguir = input("¿ Desea adivinar otra palabra ?: ").upper()
    if seguir == "SI":
        nuevoJuego = True
    elif seguir == "NO":
        nuevoJuego = False
    return nuevoJuego

def printInterfaz(palabra_a_adivinar,puntos,mensaje,letra_derrota,letras_usadas):
    """
    Imprime en la consola la interfaz del videojuego: La palabra a adivinar, los puntos, un mensaje que informa si el jugador acerto la partida o no,
    las letras equivocadas, y todas las letras utilizadas hasta el momento, sean incorrectas o no.
    [Hecha por: Micael Virgilio]
    """
    return f"Palabra a adivinar: {cadenaInterrogacion(palabra_a_adivinar, letras_usadas)} <{mensaje}> \nPuntos: {puntos} | Letras usadas: {letras_usadas} | Letras incorrectas: {letra_derrota}"

def inputLetra(letras_usadas):
#     Agustín Conti: Pide al usuario que ingrese una letra y verifica que sea apropiada
    letra_ingresada=str(input("Ingrese letra: ")).casefold()
    if letra_ingresada!="0" and letra_ingresada!= "fin":
        while (not letra_ingresada.isalpha() or len(letra_ingresada)!=1 or letras_usadas.count(letra_ingresada) != 0):
            if  letras_usadas.count(letra_ingresada) != 0:
                print (f"La letra \"{letra_ingresada}\" ya fue ingresada.")
            else:
                print ("Ingreso inválido")
            letra_ingresada=str(input("Ingrese letra: ")).casefold()
    letras_usadas.append(letra_ingresada)
    return letra_ingresada

def darPuntos(letra_ingresada, palabra_a_adivinar):
    """
    Retorna verdadero si la letra ingresada esta dentro de la palabra a adivinar.
    [Hecha por: Micael Virgilio]
    """
    return True if palabra_a_adivinar.count(letra_ingresada)!=0 else False

def nuevaPartida(puntajeAnterior, palabraParaJuego):
    """
    Comienza una nueva partida, con el puntaje de la partida anterior.
    [Hecha por: Micael Virgilio]
    """
    system("cls")
    letras_usadas=[]
    letra_ingresada=""
    letras_derrota=[]
    MENSAJE_ACIERTO = "¡Has Acertado una letra!"
    MENSAJE_DESACIERTO = "¡Letra incorrecta, sigue intentando!"
    puntos = puntajeAnterior
    palabra_a_adivinar = palabraParaJuego
    print("------ EL JUEGO DEL AHORCADO ------")
    print("")
    print("---------------")
    print("Instrucciones:")
    print("     - Solo se permite una letra por ingreso.")
    print("     - Solo se permiten letras.")
    print("     - Para salir del juego ingrese: \"fin\" o \"0\".")
    print("---------------")
    print("")
    print(f"Palabra a adivinar: {cadenaInterrogacion(palabra_a_adivinar, letras_usadas)} | Puntos: {puntos} | Letras incorrectas: {letras_derrota}")
    print("")
    while not victoria(letras_usadas, palabra_a_adivinar) and letra_ingresada!="fin" and letra_ingresada!="0":
        letra_ingresada=inputLetra(letras_usadas)
        if darPuntos(letra_ingresada, palabra_a_adivinar):
            puntos += 10
            print("")
            print(printInterfaz(palabra_a_adivinar,puntos,MENSAJE_ACIERTO,letras_derrota,letras_usadas))
        else:
            puntos -= 5
            letras_derrota.append(letra_ingresada)
            print("")
            print(printInterfaz(palabra_a_adivinar,puntos,MENSAJE_DESACIERTO,letras_derrota,letras_usadas))
    if victoria(letras_usadas, palabra_a_adivinar):
        print("")
        print("¡Felicidades, has adivinado la palabra!")
    seguir = preguntarNuevoJuego()
    if seguir:
        palabraParaJuego = obtenerPalabra(palabras_candidatas(), longitud_deseada())
        nuevaPartida(puntos,palabraParaJuego)
    else:
        print("")
        print(f"GAME OVER | Puntos totales: {puntos}")

def ejecutarJuego(palabraParaJuego):
    """
    Es la funcion principal, la cual ejecuta el juego por primera vez.
    [Hecha por: Micael Virgilio]
    """
    system("cls")
    letras_usadas=[]
    letra_ingresada=""
    letras_derrota=[]
    MENSAJE_ACIERTO = "¡Has Acertado una letra!"
    MENSAJE_DESACIERTO = "¡Letra incorrecta, sigue intentando!"
    puntos = 0
    palabra_a_adivinar = palabraParaJuego
    print("------ EL JUEGO DEL AHORCADO ------")
    print("")
    print("---------------")
    print("Instrucciones:")
    print("     - Solo se permite una letra por ingreso.")
    print("     - Solo se permiten letras.")
    print("     - Para salir del juego ingrese: \"fin\" o \"0\".")
    print("---------------")
    print("")
    print(f"Palabra a adivinar: {cadenaInterrogacion(palabra_a_adivinar, letras_usadas)} | Puntos: {puntos} | Letras incorrectas: {letras_derrota}")
    print("")
    while not victoria(letras_usadas, palabra_a_adivinar) and letra_ingresada!="fin" and letra_ingresada!="0":
        letra_ingresada=inputLetra(letras_usadas)
        if darPuntos(letra_ingresada, palabra_a_adivinar):
            puntos += 10
            print("")
            print(printInterfaz(palabra_a_adivinar,puntos,MENSAJE_ACIERTO,letras_derrota,letras_usadas))
        else:
            puntos -= 5
            letras_derrota.append(letra_ingresada)
            print("")
            print(printInterfaz(palabra_a_adivinar,puntos,MENSAJE_DESACIERTO,letras_derrota,letras_usadas))
    if victoria(letras_usadas, palabra_a_adivinar):
        print("")
        print("¡Felicidades, has adivinado la palabra!")
    seguir = preguntarNuevoJuego()
    if seguir:
        palabraParaJuego = obtenerPalabra(palabras_candidatas(), longitud_deseada())
        nuevaPartida(puntos,palabraParaJuego)
    else:
        print("")
        print(f"GAME OVER | Puntos totales: {puntos}")

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
    longitud = longitudDeseada
    lista_de_palabras = diccionarioDePalabras
    palabras_filtradas = filtrar_palabras(lista_de_palabras,longitud)
    palabra_elegida = random_word(palabras_filtradas)
    return palabra_elegida

def main():
    palabraParaJuego = obtenerPalabra(palabras_candidatas(), longitud_deseada())
    system("cls")
    ejecutarJuego(palabraParaJuego)

main()