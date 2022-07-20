"""
Proyecto Básico de Python (El Ahorcado).
Basado en el proyecto de: Kylie Ying (@kylieyying). 
"""
import random #obtener números aleatorios
import string #obtener cadena de carácteres
from palabras import palabras 
from ahorcado_diagramas import vidas_diccionario_visual


def obtener_palabra_válida(palabras): #constructor hace referencia al objeto creado
    palabra = random.choice(palabras) #Inicializamos los atributos dandole valor


    while '-' in palabra or ' ' in palabra:#ejecuta un bloque de código de la lista palabras
        palabra = random.choice(palabras)

    return palabra.upper()#de la lista palabras devulve una cadena en mayúsculas


def ahorcado(): #funcion sin argumento

    print("=======================================") #Muestra la bienvenida al jugador
    print(" ¡Bienvenido(a) al juego del Ahorcado! ")
    print("=======================================")

    palabra = obtener_palabra_válida(palabras)#asigna valor a la palabra de la lista palabras válidas.
    letras_por_adivinar = set(palabra) #palabra que aparecera sin un orden de la lista palabras.
    abecedario = set(string.ascii_uppercase) #palabras en mayúsculas
    letras_adivinadas = set() #letras adivinadas pertenecen a las lista de letras por adivinar.

    vidas = 7 #asignación de la variable vidas


    while len(letras_por_adivinar) > 0 and vidas > 0:  #Inicialización de un bucle mientras las letras por adivinar sean menor a 0 y el número de vidas tambíen a 0 el programa muestra las vidas qye sobran y las letras que se han adivinado.

        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")

      
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]#si de la lista palabras, letra esta en letras adivinadas se revisa la lista de palabras.
        print(vidas_diccionario_visual[vidas]) #Muestra los intentos
        print(f"Palabra: {' '.join(palabra_lista)}") 

     
        letra_usuario = input('Escoge una letra: ').upper() #El usuario ingresa una letra por consola la cual se convierte en mayúscula.

        if letra_usuario in abecedario - letras_adivinadas:#si la letra del usuario esta en la lista abecedatio y en la lista adivinada la letra usuario se agrega a las letras adivinadas.
            letras_adivinadas.add(letra_usuario)
       
            if letra_usuario in letras_por_adivinar: #si la letra usuario esta en letras por adivinar se elinima la letra ingresada por el usuario de la lista y se muestra.
                letras_por_adivinar.remove(letra_usuario)
                print('')
         
            else:
                vidas = vidas - 1 #Si no sucede lo anterior se elimina una vida del contador a la vez que se muestra que la letra que ingreso no se encuentra en la palabra. 
                print(f"\nTu letra, {letra_usuario} no está en la palabra.")
        
        elif letra_usuario in letras_adivinadas: #si la letra ingresada por el usuario esta en lista de letras adivinadas se imprime el texto que ya escogio esa letra y le solicita otra letra.Falta colocar un input para facilitar el ingreso de otra letra.Si ingresa otro caracter marca un error.
            print("\nYa escogiste esa letra. Por favor escoge una letra nueva.")
        else:
            print("\nEsta letra no es válida.")

   
    if vidas == 0:#Si el número de vidas es igual a 0, se muestra el texto de que ha perdido los intentos y la palabra correspondiente.Si ingresa la palabra correspondiente aparece un texto de felicidades y la palabra adivinada.
        print(vidas_diccionario_visual[vidas])
        print(f"¡Ahorcado! Perdiste. Lo lamento mucho. La palabra era: {palabra}")
    else:
        print(f'¡Excelente! ¡Adivinaste la palabra {palabra}!')


    ahorcado() #Inicia de nueva el programa
