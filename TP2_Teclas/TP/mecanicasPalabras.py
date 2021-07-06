import random

def leerLinea(archivo):
    
    """
    Lee una linea del archivo que le des
    y devuelve una lista de palabras
    [Hecha por: Agustín Conti con la
     ayuda de Juan Ignacio D`Angona]
    """
    linea = archivo.readline()
    if linea:
        linea = ((linea.casefold()).replace(".","").replace(",","")).split()
    else:
        linea="jjjjjjjjjjjjjjjjj"
    return linea

def sacarTildes(palabra):
    """
    Devuelve la cadena ingresada sin
    tildes si las tenia
    [Hecha por: Agustín Yanuchausky]
    """
    
    reemplazos = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in reemplazos:
        palabra = palabra.replace(a, b)
    return palabra

def agregarDiccionario(linea,diccionario_palabras,numero_archivo):  
    """
    Agrega las palabras de la 
    linea dada al diccionario
    [Hecha por: Agustín Conti con la
     ayuda de Juan Ignacio D`Angona]
    """
    
    LONG_PALABRA_MIN= leerConfig("LONG_PALABRA_MIN")
    
    for palabra in linea:
        palabra=sacarTildes(palabra)
        palabra = ''.join(filter(str.isalpha, palabra))
        if (palabra.isalpha()) and len(palabra)>= int(LONG_PALABRA_MIN):
            if palabra not in diccionario_palabras:
                lista=[0,0,0]
            else:
                lista=diccionario_palabras[palabra]
            if palabra not in diccionario_palabras:
                lista[numero_archivo]= 1
                diccionario_palabras[palabra]=lista
            else:
                lista[numero_archivo]+=1
                diccionario_palabras[palabra]=lista
    return diccionario_palabras
    
def leerArchivo(archivo,numero_archivo,diccionario):
    
    """
    Lee el archivo dado y llama
    a las otras funciones
    [Hecha por: Agustín Conti con la
     ayuda de Juan Ignacio D`Angona]
    """
    
    fin_de_archivo="jjjjjjjjjjjjjjjjj"
    
    lineaArchivo= leerLinea(archivo)

    while lineaArchivo != fin_de_archivo:
        if lineaArchivo != [] and lineaArchivo!=fin_de_archivo:
            diccionario=agregarDiccionario(lineaArchivo,diccionario,numero_archivo)
            
        lineaArchivo= leerLinea(archivo)

    return diccionario

def diccionarios():
    
    """
    Abre los archivos de texto
    y devuelve el diccionario completo
    [Hecha por: Agustín Conti]
    """    
    
    cuentos= open ("Cuentos.txt","r")
    la_araña_negra= open ("La araña negra - tomo 1.txt","r")
    mil_y_una_noches= open ("Las 1000 Noches y 1 Noche.txt","r")
    
    diccionario={}
    
    diccionario=leerArchivo(cuentos,0,diccionario)
    cuentos.close()
    
    diccionario=leerArchivo(la_araña_negra,1,diccionario)
    la_araña_negra.close()
    
    diccionario=leerArchivo(mil_y_una_noches,2,diccionario)
    mil_y_una_noches.close()
    
    crearArchivoPalabras(diccionario)
    
    return diccionario

def crearArchivoPalabras(diccionario):
        
    """
    Crea un csv con las palabras
    candidatas y cuantas veces
    aparecen estas en los textos
    [Hecha por: Agustín Conti]
    """
    
    archivo_palabras=open("palabras.csv","w")
    
    lista_palabras = sorted(diccionario.items())
    
    for lista in lista_palabras:
        archivo_palabras.write(str(lista[0]))
        archivo_palabras.write(",")
        archivo_palabras.write(str(lista[1][0]))
        archivo_palabras.write(",")
        archivo_palabras.write(str(lista[1][1]))
        archivo_palabras.write(",")
        archivo_palabras.write(str(lista[1][2]))
        archivo_palabras.write("\n")
        
    archivo_palabras.close()

def leerConfig(parametro):
    """
    Según el parametro dado lee este
    del archivo y devuelve su valor
    [Hecha por: Juan Ignacio D`Angona]
    """
    config= open ("configuracion.csv","r")
    while config:
        linea= config.readline()
        linea= (linea.replace(","," ").replace("\n","")).split()
        if linea[0]==parametro:
            config.close()
            return linea[1]

def longitudDeseada():
    """
    Pide al usuario que ingrese
    la longitud que quiere.
    Devuelve una random si
    no se ingresa nada
    [Hecha por: Maria Zahra]
    """
    ingresar_long = input("Ingrese la longitud deseada para la palabra: ")
    while not ingresar_long.isdecimal() and ingresar_long == "":
        if ingresar_long == "":
            ingresar_long=str(random.randint(5, 15))
        elif not ingresar_long.isdecimal():    
            ingresar_long = input("Ingreso inválido, solo se permiten números enteros: ")
    return int(ingresar_long)

def filtrarPalabras(lista_de_palabras,longitud):
    """
    Crea una lista con palabras
    con longitud válida
    [Hecha por: Maria Zahra]
    """
    palabras_candidatas = []
    palabras_no_candidatas = 0
    if(longitud == -1):
        palabras_candidatas = lista_de_palabras
    else:
        for palabra in lista_de_palabras:
            if len(palabra) == longitud:
                palabras_candidatas += [palabra]
            elif len(palabra) != longitud:
                palabras_no_candidatas += 1
    if palabras_no_candidatas == len(lista_de_palabras):
        ingresar_nueva_longitud = int(input("No hay palabras la longitud deseada en el texto. Ingrese otra longitud: "))
        palabras_candidatas = filtrarPalabras(lista_de_palabras,ingresar_nueva_longitud)
    return palabras_candidatas

def palabraRandom(lista_de_candidatas):
    """
    Elige una palabra random
    de la lista de posibles
    [Hecha por: Maria Zahra]
    """
    palabra_elegida = lista_de_candidatas[random.randint(0,len(lista_de_candidatas) - 1)]
    return palabra_elegida

def obtenerPalabra(diccionarioDePalabras, longitudDeseada = -1):
    """
    Llama a las demás funciones
    para obtener una palabra
    [Hecha por: Maria Zahra]
    """
    longitud = longitudDeseada
    lista_de_palabras = diccionarioDePalabras
    palabras_filtradas = filtrarPalabras(lista_de_palabras,longitud)
    palabra_elegida = palabraRandom(palabras_filtradas)
    return palabra_elegida

def inputLetra(letras_usadas):
    """
    Pide al usuario que ingrese una
    letra y verifica que sea apropiada
    [Hecha por: Agustín Conti]
    """
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