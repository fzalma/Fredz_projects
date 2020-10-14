from FINAL.classes_final import Tablero

#The two Tablero objects we will use to play
user_tab=Tablero("User_Boats",10,10)
machine_tab=Tablero("Machine_Boats",10,10)

#those lists are here to record the different shoots done for the user and the machine, to avoid to have two shoots on the same point.
user_lista = []
machine_lista = []


