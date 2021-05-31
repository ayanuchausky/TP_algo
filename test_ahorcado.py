letras_usadas=[]
aciertos=0
desaciertos=0
palabra_a_adivinar = "autos"

def palabra_insertada_a_interrogacion(palabra_a_adivinar):
#     Agustín Conti: Crea una cadena de interrogaciones igual de larga que la palabra
    interrogaciones=""
    for caracter in palabra_a_adivinar:
        if letras_usadas.count(caracter) != 0:
            interrogaciones += caracter
        else: 
            interrogaciones += "?"
    return interrogaciones

def print_interfaz(palabra_a_adivinar):
#     Agustín Conti: Imprime la interfaz del juego
    print("Palabra a adivinar:",palabra_insertada_a_interrogacion(palabra_a_adivinar), "Aciertos: ",aciertos , "Desaciertos: ",desaciertos)

def ingrese_letra():
#     Agustín Conti: Pide al usuario que ingrese una letra y verifica que sea apropiada
    letra_ingresada=str(input("Ingrese letra: ")).casefold()
    while (not letra_ingresada.isalpha() or len(letra_ingresada)!=1 or letras_usadas.count(letra_ingresada) != 0):
        if  letras_usadas.count(letra_ingresada) != 0:
            print (letra_ingresada, "ya fue ingresada")
        else:
            print ("Ingreso inválido")
        letra_ingresada=str(input("Ingrese letra: ")).casefold()
    letras_usadas.append(letra_ingresada)

def victoria():
#     agregar funcion que verifique que todas las letras ya fueron adivinadas
    pass

def main():
    CANTIDAD_DESACIERTOS_PERDER= 8
    while desaciertos<=CANTIDAD_DESACIERTOS_PERDER and not victoria():
        print_interfaz(palabra_a_adivinar)
        ingrese_letra()
        palabra_insertada_a_interrogacion(palabra_a_adivinar)











main()