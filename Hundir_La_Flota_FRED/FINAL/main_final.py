from FINAL.funciones_final import *


#main

print("\n ----------------------"
      "\n -Welcome to the Game--"
      "\n ----------------------")

#colocacion automatica de los barcos

user_tab.colocacion_automatica()
machine_tab.colocacion_automatica()

print("This is your board with your boats generated automatically"
      "\nYou will see on it where the machine will hit your board"
      "\nIt will show XX if it hits a boat, _ if it hits water"
      "\nYou will see also your shoots with the same symbols on your Shoot Zone"
      "\n")

user_tab.print_main()

print("\nReady ? Let's play!"
      "\n-------------------"
      "\nUser starts !!! ")

game("User",20,20)

#the game function starts once the player who starts is defined and the number of lives each player has
#Here we count 20 lives as per as the boats, but you can imagine having less lives for example.
