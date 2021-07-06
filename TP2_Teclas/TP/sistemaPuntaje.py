def cadenaInterrogacion(palabra_a_adivinar, letras_usadas):
    """
    Crea una cadena de interrogaciones
    igual de larga que la palabra
    [Hecha por: Agustín Conti]
    """
    interrogaciones=""
    for caracter in palabra_a_adivinar:
        if letras_usadas.count(caracter) != 0:
            interrogaciones += caracter
        else: 
            interrogaciones += "?"
    return interrogaciones

def victoria(letras_usadas, palabra_a_adivinar):
    """
    Si todas las letras fueron
    adivinadas retorna un True
    [Hecha por: Agustín Conti]
    """
    ganar=False
    if cadenaInterrogacion(palabra_a_adivinar,letras_usadas).count("?")==0:
        ganar=True
    return ganar

def darPuntos(letra_ingresada, palabra_a_adivinar):
    """
    Retorna verdadero si la letra ingresada esta dentro de la palabra a adivinar.
    [Hecha por: Micael Virgilio]
    """
    return True if palabra_a_adivinar.count(letra_ingresada)!=0 else False