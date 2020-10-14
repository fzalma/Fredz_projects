import numpy as np
import time

from FINAL.variables_final import *

#the game is defined under a function to have a clean main

def game(turn: object = None, machine_lives: object = None, user_lives: object = None) -> object:
    while True:
        if turn == "User":
            user_shoot_long = int(input("Let´s shoot with a longitude (from 0 to 9)..."))
            user_shoot_lati = int(input("... and with a latitude (from 0 to 9)"))

            if user_shoot_long in range(10) or  user_shoot_lati in range(10):

                if [user_shoot_long, user_shoot_lati] not in user_lista:
                    user_lista.append([user_shoot_long, user_shoot_lati])

                    x = machine_tab.user_hit_or_not(user_shoot_long, user_shoot_lati)

                    if x is True:

                        print("\nHIT!!"
                              "\n")
                        time.sleep(2)
                        machine_lives -= 1

                        if machine_lives == 0:
                            print("\nUser WINS")
                            break
                        user_tab.print_main()
                        machine_tab.print_shoot_zone()
                        time.sleep(3)

                        print("\nMachine's remaining lives :", machine_lives)
                        print("\nUser plays again")
                        time.sleep(3)

                        turn = "User"

                    else:

                        print("\nWATER!"
                              "\n")
                        time.sleep(2)

                        user_tab.print_main()
                        machine_tab.print_shoot_zone()
                        time.sleep(3)

                        print("\nIt is now Machine's turn...")
                        time.sleep(3)

                        turn = "Machine"

                else:
                    print("\nAlready done! Try something else!"
                          "\n")
                    turn = "User"

            else:
                print("\nWrong inputs. Try again"
                      "\n")
                turn = "User"


        elif turn == "Machine":
            machine_shoot_long = np.random.randint(10)
            machine_shoot_lati = np.random.randint(10)

            if [machine_shoot_long, machine_shoot_lati] not in machine_lista:
                machine_lista.append([machine_shoot_long, machine_shoot_lati])
                x = user_tab.machine_hit_or_not(machine_shoot_long, machine_shoot_lati)

                if x is True:
                    print("\nHIT!!"
                          "\n")
                    time.sleep(2)

                    user_lives -= 1

                    if user_lives == 0:
                        print("\n Machine WINS")
                        break
                    user_tab.print_main()
                    machine_tab.print_shoot_zone()
                    time.sleep(3)

                    print("\nUser's remaining lives :", user_lives)
                    print("\nMachine plays again")

                    turn = "Machine"

                else:
                    print("WATER !"
                          "\n")
                    time.sleep(2)

                    user_tab.print_main()
                    machine_tab.print_shoot_zone()
                    time.sleep(3)

                    print("\nIt is now User's turn..."
                          "\n")
                    turn = "User"

            else:
                turn = "Machine"