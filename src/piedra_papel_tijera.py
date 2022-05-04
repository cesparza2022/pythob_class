''' Name 
    Piedra, papel o tijera
    
Version
    1.1
    
Author 
    Cesar Esparza

Github
  https://github.com/cesparza2022/pythob_class
    
Description
    Es un script para que un usuario pueda jugar piedra, papel o tijera con la computadora. 
    

Category
    Entretenimiento

INPUT
    nombre
    "piedra", "papel" o "tijera"
    Solicita al usuario si queire jugar otra partida
    
OUTPUT

    Su eleccion y la generada aleatoriamente por la computadora
    Resultado de la partida
    
ARGUMENTS
    none

SEE ALSO
    none
'''

#importar el modulo para poder obtener valores aleatorios
import random

#Definir la s opciones
opciones = ["piedra", "papel", "tijera"]

#Declarar la variable que va a controlar el ciclo como verdadera
jugar_otra = "si"

#Pedir el nombre, y su decision al usuario
nombre = input("Bienvenido al juego de piedra, papel o tijera \nDame tu nombre: ")

#Crear el ciclo con el que despues de cada partida se pregunta si quiere seguir jugando
while jugar_otra.lower() =="si": 
  decision = input(f"{nombre} escoge a la cuenta de tres (piedra, papel o tijera): ")
  decision = decision.lower()
  
  #Obtener con la funcion random uno de las opciones de forma aleatoria 
  compu= random.choice(opciones)
  print(f"\n {nombre}: {decision} \n Computadora: {compu}.\n")
  
  #Cuando el usuario y la computadora tienen lo mismo
  if decision == compu:
    print("Empate. No ganar es perder.")
  
  
  #Cuanodo el usuario escoge papel 
    #La computadora tiene piedra el usuario gana
    #No es empate y la computadora no tiene roca el usuario pierde
  elif decision == "papel":
      if compu == "piedra": 
          print(f"Felicidades {nombre} ganaste")
      else:
          print(f"Perdiste {nombre} jijijaja")
  
  #Cuanodo el usuario escoge tijera 
    #La computadora tiene papel el usuario gana
    #No es empate y la computadora no tiene papel el usuario pierde
  elif decision == "tijera":
      if compu == "papel":
          print(f"Felicidades {nombre} ganaste")
      else:
          print(f"Perdiste {nombre} jijijaja")
  
  #Cuanodo el usuario escoge piedra
    #La computadora tiene tijera el usuario gana
    #No es empate y la computadora no tiene tijera el usuario pierde
  elif decision == "piedra":
      if compu == "tijera":
          print(f"Felicidades {nombre} ganaste")
      else:
          print(f"Perdiste {nombre} jijijaja")

  jugar_otra =input("¿Quieres seguir juando? (si/no)")

print("Gracias por jugar")
