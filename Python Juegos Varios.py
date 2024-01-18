
#Desarrollado por: FRANCISCO VELASCO
#Este proyecto es un conjunto de cuatro juegos básicos hechos en Python, es necesario descargar la librería "turtle" antes de ejecutar!

#Definición de variables para el Programa 1

import random #biblioteca de números random
import time #para controlar el tiempo
from os import system
import turtle
nIntentos=0
intento=0
nRandom=0
rMin=1
rMax=50
consola = True #Para manejar el programa  
    
#Definición de variable Programa 2

elementos= ["agua","nieve","fuego"]
bot=""

#Definición de variable Programa 3
progreso=[]
palabras = []
resultado = []
#FUNCIONES DEL AHORCADO
def imprimirAhorcado():
    if errores == 6:
        print("""
                       ___
                      |   |
                     _O/  |
                      |   |
                     / \  |
                    *******
        """)
        print("\n Lo siento, haz perdido..")
    elif errores == 5:
        print("""
                       ___
                      |   |
                     _O/  |
                      |   |
                       \  |
                    *******
        """)
    elif errores == 4:
        print("""
                       ___
                      |   |
                     _O/  |
                      |   |
                          |
                    *******
        """)
    elif errores == 3:
        print("""
                       ___
                      |   |
                     _O/  |
                          |
                          |
                    *******
        """)
    elif errores == 2:
        print("""
                       ___
                      |   |
                      O/  |
                          |
                          |
                    *******
        """)
    elif errores == 1:
        print("""
                       ___
                      |   |
                      O   |
                          |
                          |
                    *******
        """)
    elif errores == 0:
        print("""
                       ___
                      |   |
                          |
                          |
                          |
                    *******
        """)
    return ""
def obtenerPalabra():
    categorías = """ 
 Por favor, selecciona la categoría con la que quieres jugar:
 
    Categorías:
    1. Animales
    2. Países
    3. Lenguajes de Programación
    4. VideoJuegos
    5. Marcas Famosas (varios)
    """
    while True:
        try:    
          print(categorías)
          op= int(input("Mi selección es: "))
          if (op<=0 or op>5):
            raise Exception
        except Exception:
          print("No se pueden ingresar letras, números negativos o decimales. Intenta nuevamente..")
          print("*Recuerda que las opciones son (1/2/3/4/5)*")
          input("\nPRECIONA ENTER PARA CONTINUAR ")
          system("cls")
        else: break
        
    if op is 1: 
        palabras=["perro", "gato", "cangrejo","jirafa","lobo","conejo", "leopardo", "oso","caballo","ballena","gorila","cocodrilo","dinosaurio","águila"]
    elif op is 2:
        palabras=["ecuador", "japón", "francia","polonia","colombia","argentina", "guatemala", "canada","noruega","holanda","italia","españa","corea","alemania"]
    elif op is 3:
        palabras=["ruby", "csharp", "java","python","perl","php","scala","c","matlab","swift","typescript","rust","golang"]
    elif op is 4:
        palabras=["crashbandicoot", "tetris", "supermario","zelda","minecraft","fifa","smashbros","pacman","gta","counterstrike","pong","persona","castlevania","lunarknights","ghosttrick"]
    elif op is 5:
        palabras=["apple", "samsung", "microsoft", "nike", "adidas", "cocacola", "pepsi", "playstation", "sony", "nintendo", "crunchyroll","amazon"]
    return palabras 
def palabraPro():
   palabras=obtenerPalabra()
   palabra = random.choice(palabras).upper()
   return palabra

#Variables iniciales Snake Programa 4

puntaje=0
record=0

#Calculadora (Extras):
def operaciones():

    operaciones = """ 
 Por favor, selecciona la categoría con la que quieres trabajar:
 
    Categorías:
    1. Extraer un rango de palabras de una frase
    2. Reemplazar una palabra de una frase
    """
    while True:
        try:    
          print(operaciones)
          op= int(input("Mi selección es: "))
          if (op<=0 or op>2):
            raise Exception
        except Exception:
          print("No se pueden ingresar letras, números negativos o decimales. Intenta nuevamente..")
          print("*Recuerda que las opciones son (1/2)*")
          input("\nPRECIONA ENTER PARA CONTINUAR ")
          system("cls")
        else: break
        
    if op is 1: 
        system("cls")
        frase = input("Escribe tu frase: ")
        inicial = (int(input("Escribe la posición inicial: ")))
        final = (int(input("Escribe la posición final: ")))
        rango = slice(inicial,final) #Simulación del substring
        frase2 = frase[rango]
        resultado = print("Haz extraído: " + frase2)

    elif op is 2:
       system("cls")
       frase = input("Escribe tu frase: ")
       palabra = input("Escribe la palabra a reemplazar: ")
       palabra2 = input("Escribe la nueva palabra: ") 
       x = frase.replace(palabra, palabra2) #Reemplazo de palabras
       resultado = print(x)
    return resultado 


#MENU DE OPCIONES

menu = """ 
Menu:
1. JUEGO DEL NÚMERO AL AZAR
2. JUEGO: "AGUA, NIEVE O FUEGO"
3. JUEGO DEL AHORCADO 
4. SUPER SNAKE 
5. EXTRAS
6. SALIR
"""
while consola == True: #simulación de Do-While, entra al bucle SÍ o SÍ
    system("cls")
    while True:
        try:   
          print(menu)    
          op= int(input("Mi selección es: "))
          if (op<=0 or op>6):
              raise Exception
        except Exception:
          print("No se pueden ingresar letras, números negativos o decimales. Intenta nuevamente..")
          print("*Recuerda que las opciones son (1/2/3/4)*")
          input("\nPRECIONA ENTER PARA CONTINUAR ")
          system("cls")
        else: break #Si no hay ningún error, ejecuta las opciones disponibles
        
    #----------------------------------------------------------------------------------------------------------------------
    #JUEGO NÚMERO 1     
    if op is 1:
        system("cls")
        nIntentos=0
        usuario = input("PC: Hola!, ¿Cómo te llamas?: ")
        nRandom = random.randint(rMin,rMax)
        print("De acuerdo " + usuario + ", estoy pensando en un número entre 1 y 50")
        print("**Tienes 6 intentos**")
        while nIntentos<6:
            while True: #Do-While de expeciones
                try:
                 intento =(int(input("\nIntenta adivinar mi número: ")))
                 nIntentos += 1
                 if (intento<=0 or intento>50): #Si el número sobrepasa los límites hay excepción
                     raise Exception        
                except Exception:
                 print("*Recuerda el rango (1-50)*")
                 print("No se pueden ingresar letras o números negativos, intenta nuevamente..")
                else: break

            if (intento<nRandom): #Si el intento de adivinar es menor al número se informa
                print("PC: Número muy bajo, prueba otro..")
            elif(intento>nRandom): #Si el intento de adivinar es mayor al número se informa
                print("PC: Número muy alto, prueba otro..")
            elif(intento==nRandom):
                break     

        if intento == nRandom: #Si el número adivinado coincide con el del bot, el usuario ha ganado
            nIntentos=str(nIntentos)
            print("\nMuy bien " + usuario + "! lograste adivinar mi número en " +nIntentos+" intentos")
        else:
            nRandom=str(nRandom) #Sino, ha perdido
            print("\nLo siento " + usuario + ", el número que estaba pensando era el " +nRandom)
        print("\n *El Juego Ha Finalizado*")
        input("PRECIONA ENTER PARA CONTINUAR ")
    #----------------------------------------------------------------------------------------------------------------------
    #JUEGO NÚMERO 2
    elif op is 2:
        system("cls")
        print("\n Muy bien! ¿¡Creés que tienes lo necesario para ganarme!? \n Reglas: \n- Fuego >> Nieve \n- Nieve >> Agua \n- Agua >> Fuego")
        print("\n ¡¡HORA DE JUGAR!!")
        while True:
         try:
           usuario =(input("\nPC: Vamos! elige tu elemento, ¿(Agua, Nieve o Fuego)?: ")).lower()  
           if usuario not in elementos:
               raise Exception  
         except Exception:
            print("\nElemento inválido, intenta nuevamante..")
            print("*Recuerda que las opciones son (Agua, Nieve o Fuego)*")
            input("\nPRECIONA ENTER PARA CONTINUAR ")
            system("cls")
         else: break
        bot= random.choice(elementos) #La computadora escoge una opción al azar
        time.sleep(1.4) #Reposo de tiempo para darle un mejor toque al juego
        print("\n¡La computadora eligió "+ bot + "!")
        time.sleep(0.8)
        if usuario==bot: #Si ambos eligieron lo mismo, hay empate
         print("\n ¡Empate!")
         print("PC: Vaya vaya, parece que ambos elegimos "+usuario+" (ㆆ_ㆆ)")
        #Comprobación de las distintas posibilidades de ganar
        elif bot=="fuego" and usuario=="agua":
         print("\n ¡Felicidades!, Me haz ganado (ツ)👌")
         print("*El agua le gana al fuego*")

        elif bot=="nieve" and usuario=="fuego":
         print("\n ¡Felicidades!, Me haz ganado (ツ)👌")
         print("*El fuego le gana a la nieve*")

        elif bot=="agua" and usuario=="nieve":
         print("\n ¡Felicidades!, Me haz ganado (ツ)👌")
         print("*La nieve le gana al agua*")
        #Si el bot gana, se informa
        else:
         print("\n Lastima, no lograste ganarme.. ( ͡≖ ᴗ ͡≖)")
         print("*"+ usuario + " pierde contra "+bot+"*")
         time.sleep(0.8)
        print("\n *El Juego Ha Finalizado*")
        input("PRECIONA ENTER PARA CONTINUAR ")
        
    #----------------------------------------------------------------------------------------------------------------------    
    #JUEGO NÚMERO 3
    elif op is 3:
        system("cls")
        palabra = palabraPro() #A partir de la categoría, obtiene un elemento al azar
        errores = 0 #Reinicio de errores
        progreso = [] #Reinicio de progreso
        for i in range(len(palabra)): #Recorre el indice de la palabra random (igual que un arreglo)
            progreso.append("_ ") #Por cada letra de la palabra, pondrá un guión bajo y un espacio 

        palabra_con_espacios = [] #Reinicio de palabra con espacios
        for char in palabra: #Agrega a un arreglo donde cada letra de la palabra tendrá un espacio
            palabra_con_espacios.append(char + ' ') 

        letras_usadas = [] #Reinicio del progreso (letras)
        while errores <= 6: #Siempre y cuando el usuario tenga menos de 6 errores, funciona el programa          
            while True: #Do-While de expeciones
             system("cls") #Limpia la consola
             imprimirAhorcado() #Llama a la función para imprimir el ahorcado
             print(''.join(progreso)) #Convierte el arreglo en un string vacío, añadiendole todos los elementos de progreso
             print("\nLetras usadas: ", letras_usadas) #Imprime el arreglo con las palabras usadas

             try:           
                 letra =(input("\nPC: Vamos! elige tu letra: ")).upper()  
                 if len(letra)!=1: #Si el usuario ingresa más de una letra, se genera una excepción
                    raise Exception
                 if letra.isalpha(): #Si solo existe un dígito de una letra existente, sale del bucle
                    break
                 else: raise Exception #Si el usuario ingresa números o carácteres especiales, se genera una expeción
             except Exception:
                print("\nElemento inválido, intenta nuevamante..")
                print("*Recuerda que no puedes ingresar carácteres especiales o números*")
                input("\nPRECIONA ENTER PARA CONTINUAR ")
                system("cls")

            if letra in letras_usadas or letra==True: #Si el usuario repite una letra, se informa
                print("\nPC: Recuerda que ya usaste esta letra, prueba otra..")
                input("\nPRECIONA ENTER PARA CONTINUAR ")
            else:
                letras_usadas.append(letra) #Se agrega la letra al arreglo de letras usuadas
                hay_error = True #Inicializamos en true para comprobar si va existir un error
                for i in range(len(palabra)): #Recorre la palabra para realizar la comprobación
                    if letra == palabra[i]: #Si la letra de la palabra está, se agrega
                        progreso[i] = letra + ' ' #Se agrega al progreso
                        hay_error = False #Si no hay error, no se le aumenta nada

                if hay_error: #Si no coincide la letra con la palabra, se aumenta el error
                    errores += 1

                if letra==True: #Limpieza de consola en caso de excepción
                 system("cls")

                if errores == 6: #Si el usuario ha llegado a los 6 errores, pierde
                 system("cls")
                 imprimirAhorcado() #Se imprime el ahorcado
                 print("\n La palabra correcta fue:", palabra)
                 print("\n *El Juego Ha Finalizado*")
                 input("PRECIONA ENTER PARA CONTINUAR ")
                 break
                
                if palabra_con_espacios == progreso: #Si el progreso coincide con la palabra espaciada, ha ganado el usuario
                    system("cls")
                    imprimirAhorcado() #Se imprime el ahorcado
                    print(''.join(progreso)) #Se muestra la palabra final
                    print("\nPC:¡Felicidades!, haz ganado (ツ)👌")
                    print("\n *El Juego Ha Finalizado*")
                    input("PRECIONA ENTER PARA CONTINUAR ")
                    break
                
    #----------------------------------------------------------------------------------------------------------------------
    #JUEGO NÚMERO 4
    elif op is 4:
        #Configuración de la ventana
        system("cls") #Limpieza de consola
        interfaz=turtle.Screen() #Inicialización de la ventana
        interfaz.title("SUPER SNAKE POR: FRANCISCO VELASCO")
        interfaz.bgcolor("black") #Color de fondo "negro"
        interfaz.bgpic("space.gif") #Imagen de fondo
        interfaz.setup(width=600, height=600) #Establecimiento de dimensiones de la ventana
        interfaz.tracer(0) #Le da fluidez a la ejecución del juego
        #Cabeza de la serpiente
        cabeza=turtle.Turtle() #Creación de un objeto
        cabeza.speed(0)#reinicio de velocidad 
        cabeza.color("darkolivegreen3") #color del objeto
        cabeza.shape("square") #forma cuadrada
        cabeza.penup() #Elimina el rastro del objeto, una característica de la interfaz gráfica "Turtle"
        cabeza.goto(0,0) #Posición inicial "x","y"
        cabeza.direction= 'stop' #Movimiento en 0, en caso de perder y al iniciar

        #Comida (Funcionalidad similar)
        comida=turtle.Turtle() #Creación del objeto
        comida.color("red")
        comida.shape("circle") #Forma circular
        comida.penup()
        comida.goto(200,40) #Posición inicial "x","y"

        #Texto en pantalla del puntaje
        texto = turtle.Turtle() #Creación del objeto
        texto.speed(0) #velocidad 0 para que no haya movimiento
        texto.color("white") #Color blanco
        texto.penup()
        texto.hideturtle()
        texto.goto(0,260) #Posición inicial "x","y"
        texto.write("Puntaje: 0        Record: 0", align="center", font=("MS Sans Serif", 24, "bold")) #características

        #Segementos (cuerpo de la serpiente)
        segmentos=[]

        #Funciones
        #Conexión de dirección para la serpiente
        def go_up(): #Dirección hacia arriba
         cabeza.direction= 'up'

        def go_down(): #Dirección hacia abajo
         cabeza.direction= 'down'

        def go_left(): #Dirección hacia la izquierda
         cabeza.direction= 'left'

        def go_right(): #Dirección hacia la derecha
         cabeza.direction= 'right'


        def move(): #Función Movimiento
         if cabeza.direction == 'up': #Configuración de movimiento de coordenada
            y= cabeza.ycor() #obtiene la coordenada en la posición "y" y la almacena en la variable
            cabeza.sety(y+20) #actualiza el valor, para ir movimiendo a la serpiente en 20 pixeles
         #Funcionalidad similiar..
         if cabeza.direction == 'down':
            y= cabeza.ycor()
            cabeza.sety(y-20)

         if cabeza.direction == 'left':
            x = cabeza.xcor()
            cabeza.setx(x-20)

         if cabeza.direction == 'right':
            x = cabeza.xcor()
            cabeza.setx(x+20)

        #Conexión de dirección de la serpiente con el teclado
        interfaz.listen() #Detecta algún evento del teclado, (si es que ocurre)
        interfaz.onkeypress(go_up, "Up") #Si detecta la tecla (arriba), se activa la función arriba
        interfaz.onkeypress(go_down, "Down") #Si detecta la tecla (abajo), se activa la función abajo
        interfaz.onkeypress(go_left, "Left") #Si detecta la tecla (izquierda), se activa la función izquierda
        interfaz.onkeypress(go_right, "Right") #Si detecta la tecla (derecha), se activa la función derecha
    
        #Bucle principal del juego
        while True:
         interfaz.update()
         
         #Comprobación de límites (Si la serpiete toca el borde, se reinicia el marcado y la posición de la serpiente)
         if cabeza.xcor() > 260 or cabeza.xcor()< -275 or cabeza.ycor() > 195 or cabeza.ycor()< -260:
            time.sleep(1)
            cabeza.goto(0,0) #reinicio de posición "x","y"
            cabeza.direction = "stop" #movimiento detenido para la serpiente
            for segmento in segmentos: #Elimina el cuerpo de la serpiente en caso de tocar los bordes
             segmento.goto(1000,1000)
            segmentos.clear() #Reinicio de puntaje
            puntaje=0
            texto.clear() 
            texto.write("Puntaje: {}        Record: {}".format(puntaje, record), align="center", font=("MS Sans Serif", 24, "bold"))

         #Obtención de manzanas en posiciones aleatorias
         if cabeza.distance(comida)< 20: #Comprobación entre la distancia de la comida y la serpiente (20 pixeles)
            x = random.randint(-275,260) #Limitación de los bordes del juego, comida al alzar
            y = random.randint(-260,195)
            comida.goto(x,y) #Actualización de la posición nueva
            
            #Cuerpo de la serpiente
            nuevo_segmento=turtle.Turtle() #Creación de un nuevo objeto
            nuevo_segmento.color("darkolivegreen4")
            nuevo_segmento.shape("square")
            nuevo_segmento.penup()
            segmentos.append(nuevo_segmento) #Cada vez que se coma una manzana, se agrega el segmento al arreglo

            #Aumentar marcador
            puntaje += 10
            #Cambia el record si se cumple la condición
            if puntaje > record:
                record = puntaje
            
            texto.clear()
            texto.write("Puntaje: {}        Record: {}".format(puntaje, record), align="center", font=("MS Sans Serif", 24, "bold"))

         #Mover serpiente (cuerpo)
         totalSeg = len(segmentos) #Obtiene el total de segmentos(cuadraditos del cuerpo) del arreglo
         #Se decrese el número del arreglo para evitar el error de un elemento inexistente
         #Se itera desde el número mayor, el útimo número del arreglo hasta el primero, y se decrese
         for index in range(totalSeg-1,0,-1): #El último elemento del arreglo sigue al de adelante (el 5 al 4, 4 al 3 etc.)
             x = segmentos [index - 1].xcor() #Se obtienen las coordenadas "x","y" del segmento anterior
             y = segmentos [index - 1].ycor() 
             segmentos[index].goto(x,y) #dependiendo del índice se actualiza a las coordenadas que obtenga
        
         if totalSeg > 0: #Indentifica que haya elementos en el arreglo
            x = cabeza.xcor() #Obtiene las coordendas de la cabeza
            y = cabeza.ycor()
            segmentos[0].goto(x,y) #Se mueve el cuerpo en donde está la cabeza

         move()

         #Colisiones con el cuerpo
         for segmento in segmentos:
             if segmento.distance(cabeza)<20:
                 time.sleep(1)
                 cabeza.goto(0,0)
                 cabeza.direction = "stop"
                 for segmento in segmentos:
                     segmento.goto(1000,1000)
                 segmentos.clear()
                 puntaje=0
                 texto.clear()
                 texto.write("Puntaje: {}        Record: {}".format(puntaje, record), align="center", font=("MS Sans Serif", 24, "bold"))
         
         time.sleep(0.0902)    
    
    #----------------------------------------------------------------------------------------------------------------------
    #EXTRAS
    elif op is 5:
        system("cls")  #Limpieza de consola
        operaciones()  #Llama a la función operaciones
        input("PRECIONA ENTER PARA CONTINUAR ") 
        
    #----------------------------------------------------------------------------------------------------------------------
    #FINAL
    elif op is 6:
        system("cls")  
        print("¡Muchas Gracia Por Jugar!, Que tengas un excelente día")  
        input("PRECIONA ENTER PARA CONTINUAR ") 
        break

