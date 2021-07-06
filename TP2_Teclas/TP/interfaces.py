from os import system
from .sistemaPuntaje import cadenaInterrogacion

def palabraInterfaz(palabra_a_adivinar,puntos,mensaje,letra_derrota,letras_usadas,intentos):
    """
    Imprime la interfaz del juego
    [Hecha por: Micael Virgilio]
    """
    interfazText = f"\nPalabra a adivinar: {cadenaInterrogacion(palabra_a_adivinar, letras_usadas)} <{mensaje}> \nPuntos: {puntos} | Letras usadas: {letras_usadas} | Letras incorrectas: {letra_derrota} | Intentos: {intentos}" 
    return print(interfazText)

def InterfazSalida():
    """
    Imprime el aviso de que saliste
    del juego
    [Hecha por: Micael Virgilio]
    """
    system("cls")
    exitCadena = f"""------ EL JUEGO DEL AHORCADO ------

- Has salido del juego.    
    """
    return print(exitCadena)

def creditos():
    """
    Imprime los integrantes del
    TP :)
    [Hecha por: Micael Virgilio]
    """
    creditosInterfaz = f"""
-------------------------------------------------
DESAROLLADORES: - Agustín Conti         
                - Juan Ignacio D`Angona 
                - Maria Zahra           
                - Agustín Yanuchausky   
                - Micael Virgilio       
"""
    return print(creditosInterfaz)