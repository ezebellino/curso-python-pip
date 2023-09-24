import random

options = ("piedra", "papel", "tijera")

computer_wins = 0
user_wins = 0
rounds = 1

print("Bienvenido al juego de Piedra, Papel o Tijera ☺")
print("Instrucciones: 1) elige una de las opciones 2) el que gana 2 de 3 es el ganador!")

while True:
  print('*' * 10)
  print('ROUND', rounds)
  print('*' * 10)

  print('La computadora lleva ganadas =>', computer_wins,"rondas")
  print('El usuario lleva ganadas =>', user_wins,"rondas")
  
  user_opt = input("piedra, papel o tijera => ")
  user_opt = user_opt.lower()
  
  if not user_opt in options:
    print("Esa Opción no es válida")
    continue
    
  computer_opt = random.choice(options)
  
  print('User option => ', user_opt)
  print('Computer option => ', computer_opt)
  
  if user_opt == computer_opt:
    print("DRAW!")
  elif user_opt == "piedra":
    if computer_opt == "tijera":
      print("PIEDRA le gana a TIJERA")
      print("Es por esta razón que el Usuario es el Ganador!")
      user_wins += 1
    else:
      print("PAPEL le gana a la PIEDRA")
      print("Es por esta razón que Computer es el Ganador!")
      computer_wins += 1      
  elif user_opt == "papel":
    if computer_opt == "piedra":
      print("PAPEL le gana a PIEDRA")
      print("Es por esta razón que el Usuario es el Ganador!")
      user_wins += 1
    else:
      print("TIJERA le gana a PAPEL")
      print("Es por esta razón que Computer es el Ganador!")
      computer_wins += 1      
  elif user_opt == "tijera":
    if computer_opt == "papel":
      print("TIJERA le gana a PAPEL")
      print("Es por esta razón que el Usuario es el Ganador!")
      user_wins += 1
    else:
      print("PIEDRA le gana a TIJERA")
      print("Es por esta razón que Computer es el Ganador!")
      computer_wins += 1
  rounds += 1
  if computer_wins == 2:
    print('The game is Finished. Computers wins!')
    break
    
  if user_wins == 2:
    print('The game is Finished. User wins!')
    break
  
