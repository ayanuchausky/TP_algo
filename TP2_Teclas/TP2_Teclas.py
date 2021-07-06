from os import system
from TP.interfaces import *
from TP.mecanicasPalabras import *
from TP.sistemaPuntaje import *
import random

def imprimirDatos(datosPartida):
    """
    Muestra los resultados de una sola partida
    [Hecha por: Agustín Yanuchausky]
    """
    for jugador in datosPartida:
        print("RESULTADOS PARA ", jugador)
        print("Aciertos: ", datosPartida[jugador][0])
        print("Desaciertos: ", datosPartida[jugador][1])
        print("Puntaje: ", datosPartida[jugador][2])
        print("Palabra a adivinar: ", datosPartida[jugador][3])
        if victoria(datosPartida[jugador][4],datosPartida[jugador][3]):
            print(jugador, " es el GANADOR!")

def chequearSiTodosPerdieron(datosJugadores, intentosPermitidos):
    """
    Revisa el diccionario para corroborar si gana la máquina
    [Hecha por: Agustín Yanuchausky]
    """
    quedaAlgunJugadorEnPie = False
    for jugador in datosJugadores:
        if datosJugadores[jugador][1] < intentosPermitidos:
            quedaAlgunJugadorEnPie = True
    return not quedaAlgunJugadorEnPie
        
def generarDatos(jugadores , palabras):
    """
    [Hecha por: Maria Zahra]
    Inicializa un diccionario para los datos de una partida
    """
    diccionario = {}
    i = 0
    for jugador in jugadores:
        diccionario[jugador] = [ 0 , 0 , 0 , palabras[i], [] , [] , [] ]
        i += 1
    return diccionario

def ejecutarJuegoMultijugador(jugadores, palabras):
    """
    Ejecuta una partida y completa el diccionario con datos y puntajes
    [Hecha por: Agustín Yanuchausky]
    """
    registroPuntajes = generarDatos(jugadores, palabras)
    intentos = int(leerConfig("MAX_DESACIERTOS"))
    MENSAJE_ACIERTO = "¡Has Acertado una letra!"
    MENSAJE_DESACIERTO = "¡Letra incorrecta, sigue intentando!"
    letra_ingresada = ""
    hayGanador = False
    perdieronTodos = False
    jugadorSeEquivoca = False
    salir=False
    PUNTOS_ACIERTOS= int(leerConfig("PUNTOS_ACIERTOS"))
    PUNTOS_DESACIERTOS= int(leerConfig("PUNTOS_DESACIERTOS"))
    PUNTOS_ADIVINA_PALABRA= int(leerConfig("PUNTOS_ADIVINA_PALABRA"))
    PUNTOS_RESTA_GANA_PROGRAMA= int(leerConfig("PUNTOS_RESTA_GANA_PROGRAMA"))
    
    while letra_ingresada != "fin" and letra_ingresada != "0" and not hayGanador and not perdieronTodos and not salir:
        for jugador in jugadores:
            jugadorSeEquivoca = False
            if(registroPuntajes[jugador][1] < intentos):
                while not jugadorSeEquivoca and not hayGanador and not perdieronTodos and not salir:
                    print("ES EL TURNO DE ", jugador)
                    palabraInterfaz(
                            registroPuntajes[jugador][3],
                            registroPuntajes[jugador][2],
                            "",
                            registroPuntajes[jugador][6],
                            registroPuntajes[jugador][4],
                            (intentos - registroPuntajes[jugador][1])
                        )
                    letra_ingresada = inputLetra(registroPuntajes[jugador][4])
                    if darPuntos(letra_ingresada, registroPuntajes[jugador][3]):
                        registroPuntajes[jugador][2] += PUNTOS_ACIERTOS 
                        registroPuntajes[jugador][0] += 1
                        palabraInterfaz(
                            registroPuntajes[jugador][3],
                            registroPuntajes[jugador][2],
                            MENSAJE_ACIERTO,
                            registroPuntajes[jugador][6],
                            registroPuntajes[jugador][4],
                            (intentos - registroPuntajes[jugador][1])
                        )
                    elif letra_ingresada == "fin" or letra_ingresada == "0":
                        InterfazSalida()
                        salir = True
                    else:
                        jugadorSeEquivoca = True
                        registroPuntajes[jugador][2] -= PUNTOS_DESACIERTOS
                        registroPuntajes[jugador][1] += 1
                        registroPuntajes[jugador][6].append(letra_ingresada)
                        perdieronTodos = chequearSiTodosPerdieron(registroPuntajes, intentos)
                        palabraInterfaz(
                            registroPuntajes[jugador][3],
                            registroPuntajes[jugador][2],
                            MENSAJE_DESACIERTO,
                            registroPuntajes[jugador][6],
                            registroPuntajes[jugador][4],
                            (intentos - registroPuntajes[jugador][1])
                        )
                    if victoria(registroPuntajes[jugador][4], registroPuntajes[jugador][3]):
                        print("\n¡Felicidades, has adivinado la palabra!")
                        hayGanador = True
                        registroPuntajes[jugador][2] += PUNTOS_ADIVINA_PALABRA
                        imprimirDatos(registroPuntajes)
    if chequearSiTodosPerdieron(registroPuntajes, intentos):
        for jugador in jugadores:
            registroPuntajes[jugador][2] -= PUNTOS_RESTA_GANA_PROGRAMA 
        imprimirDatos(registroPuntajes)
        print("No hay ganadores")
    return registroPuntajes


def ingresarJugadores():
    """
    Genera un array de jugadores segun el máximo preestablecido en la configuracion
    [Hecha por: Agustín Yanuchausky]
    """
    jugadores  = []
    max_jugadores = int(leerConfig("MAX_USUARIOS"))
    ingresoVacio = False
    while not ingresoVacio  and  len(jugadores) < max_jugadores :
        ingreso = solicitarDatos("Ingrese el nombre de un jugador: ")
        if len(ingreso) > 0:
            if ingreso not in jugadores:
                jugadores.append(ingreso)
            else:
                print("Nombre ya ingresado.")
        else:
            ingresoVacio = True
    if (len(jugadores) == max_jugadores):
        print("Se alcanzó el máximo de jugadores.")
    return jugadores

def solicitarDatos(mensaje):
    """
    [Hecha por: Maria Zahra]
    """
    dato = input(mensaje)
    return dato 

def ordenarAlAzarEInformar(jugadores):
    """
    Mezcla el orden de los jugadores y lo muestra por pantalla
    [Hecha por: Agustín Yanuchausky]
    """
    random.shuffle(jugadores)
    print("---ORDEN DE LOS TURNOS---")
    turno = 1
    for jugador in jugadores:
        print("TURNO #" + str(turno) + " ")
        print(jugador)
        turno += 1
    return jugadores

def generarPalabras(jugadores , longitud ):
    """
    [Hecha por: Maria Zahra]
    """
    lista_de_palabras = []
    for jugador in jugadores:
        lista_de_palabras.append(obtenerPalabra(diccionarios() , longitud ))
    return lista_de_palabras

def prepararPartidaYEjecutar(jugadores):
    """
    Llama a las funciones necesarias para iniciar una partida
    [Hecha por: Agustín Yanuchausky]
    """
    jugadoresOrdenados = ordenarAlAzarEInformar(jugadores)
    longitud = longitudDeseada()
    palabrasParaJuego = generarPalabras(jugadoresOrdenados, longitud)
    return ejecutarJuegoMultijugador(jugadoresOrdenados, palabrasParaJuego)


def main():
    """
    ejecuta tantas partidas como los usuarios deseen y muestra los resultados globales
    [Hecha por: Agustín Yanuchausky]
    """
    system("cls")
    jugadores = ingresarJugadores()
    while len(jugadores)==0:
        print("Debe ingresar por lo menos 1 nombre")
        jugadores= ingresarJugadores()
    puntajesTodasLasPartidas = []
    respuesta = "SI"
    while respuesta == "SI":
        puntajesTodasLasPartidas.append(prepararPartidaYEjecutar(jugadores))
        respuesta = input("¿Desean continuar jugando? (SI/NO) ").upper()
    for jugador in puntajesTodasLasPartidas[0]:
        print("---ESTADISTICAS GLOBALES---")
        aciertosGlobales = 0
        desaciertosGlobales = 0
        puntajeGlobal = 0
        cantidadDeVictorias = 0
        palabrasJugador = []
        for partida in puntajesTodasLasPartidas:
            aciertosGlobales += partida[jugador][0]
            desaciertosGlobales += partida[jugador][1]
            puntajeGlobal += partida[jugador][2]
            palabrasJugador.append(partida[jugador][3])
            if victoria(partida[jugador][4],partida[jugador][3]):
                cantidadDeVictorias += 1
        print("Jugador ", jugador)
        print("aciertos: ", aciertosGlobales)
        print("desaciertos: ", desaciertosGlobales)
        print("puntaje: ", puntajeGlobal)
        print("victorias: ", cantidadDeVictorias)
    creditos()
    
main()