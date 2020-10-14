import numpy as np
import random


class Tablero:
    '''
    class that defines the object Tablero
    Actually there is two tablero, one called tab and the other called tab2. Tab2 is empty, when Tab will get the boats.
    Tab2 serves as a "Shoot Zone". The Shoot Zone of the Player will be displayed each time, as well as his own boat board
    The Machine shoots will be displayed directly on the User Boat Board (we dont use the Machine Shoot Zone).
    '''
    def __init__(self, id_jugador, long, lati, tab2=np.full((10, 10), " ")):
        self.long = long
        self.lati = lati
        self.tab = np.full((self.long, self.lati), " ")
        self.id_jugador = id_jugador
        self.tab2 = tab2

    def print_main(self):
        print(self.id_jugador)
        print()
        print(self.tab)
        print()

    def print_shoot_zone(self):
        print("User Shoot Zone"
              "\n")
        print(self.tab2)
        print()

    def colocacion_automatica(self):  # function to put the boats autmatically and randomly

        eslora1 = []
        eslora2 = []
        eslora3 = []
        eslora4 = []

        while True:

            orient = random.choice(['N', 'S', 'E', 'O'])
            current_pos = np.random.randint(10, size=2)
            # print(orient)
            # print(current_pos)

            fila = current_pos[0]
            col = current_pos[1]

            # Ahora hay que comprobar si esas posiciones son válidas #

            if len(eslora1) < 4:
                eslora = 1
                # Recogemos las 4 posiciones colindantes a 'current_pos'
                coors_posiN = self.tab[fila:fila - eslora:-1, col]  # he tenido que meterlo en cada 'if' porque
                coors_posiE = self.tab[fila, col: col + eslora]  # la eslora la defino dentro de cada uno
                coors_posiS = self.tab[fila:fila + eslora, col]  # si la dejaba arriba daba error puesto que
                coors_posiO = self.tab[fila, col: col - eslora: -1]  # aún no era una variable definida

                # Orientación 'N'orte:
                if orient == 'N' and 0 <= fila - eslora < 10 and '0' not in coors_posiN:
                    self.tab[fila:fila - eslora: -1, col] = '0'
                    eslora1.append(current_pos)  # hay que buscar la manera de añadirlos a una lista,diccionario...

                # Orientación 'E'ste:
                elif orient == 'E' and 0 <= col + eslora < 10 and '0' not in coors_posiE:
                    self.tab[fila, col: col + eslora] = '0'
                    eslora1.append(current_pos)

                # Orientación 'S'ur:
                elif orient == 'S' and 0 <= fila + eslora < 10 and '0' not in coors_posiS:
                    self.tab[fila:fila + eslora, col] = '0'
                    eslora1.append(current_pos)

                # Orientación 'O'este
                elif orient == 'O' and 0 <= col - eslora < 0 and '0' not in coors_posiO:
                    self.tab[fila, col: col - eslora: -1] = '0'
                    eslora1.append(current_pos)

            if len(eslora2) < 3:
                eslora = 2
                # Recogemos las 4 posiciones colindantes a 'current_pos'
                coors_posiN = self.tab[fila:fila - eslora:-1, col]
                coors_posiE = self.tab[fila, col: col + eslora]
                coors_posiS = self.tab[fila:fila + eslora, col]
                coors_posiO = self.tab[fila, col: col - eslora: -1]

                # Orientación 'N'orte:
                if orient == 'N' and 0 <= fila - eslora < 10 and '0' not in coors_posiN:
                    self.tab[fila:fila - eslora: -1, col] = '0'
                    eslora2.append(current_pos)  # hay que buscar la manera de añadirlos a una lista,diccionario...

                # Orientación 'E'ste:
                elif orient == 'E' and 0 <= col + eslora < 10 and '0' not in coors_posiE:
                    self.tab[fila, col: col + eslora] = '0'
                    eslora2.append(current_pos)

                # Orientación 'S'ur:
                elif orient == 'S' and 0 <= fila + eslora < 10 and '0' not in coors_posiS:
                    self.tab[fila:fila + eslora, col] = '0'
                    eslora2.append(current_pos)

                # Orientación 'O'este
                elif orient == 'O' and 0 <= col - eslora < 0 and '0' not in coors_posiO:
                    self.tab[fila, col: col - eslora: -1] = '0'
                    eslora2.append(current_pos)

            if len(eslora3) < 2:
                eslora = 3
                # Recogemos las 4 posiciones colindantes a 'current_pos'
                coors_posiN = self.tab[fila:fila - eslora:-1, col]
                coors_posiE = self.tab[fila, col: col + eslora]
                coors_posiS = self.tab[fila:fila + eslora, col]
                coors_posiO = self.tab[fila, col: col - eslora: -1]

                # Orientación 'N'orte:
                if orient == 'N' and 0 <= fila - eslora < 10 and '0' not in coors_posiN:
                    self.tab[fila:fila - eslora: -1, col] = '0'
                    eslora3.append(current_pos)  # hay que buscar la manera de añadirlos a una lista,diccionario...

                # Orientación 'E'ste:
                elif orient == 'E' and 0 <= col + eslora < 10 and '0' not in coors_posiE:
                    self.tab[fila, col: col + eslora] = '0'
                    eslora3.append(current_pos)

                # Orientación 'S'ur:
                elif orient == 'S' and 0 <= fila + eslora < 10 and '0' not in coors_posiS:
                    self.tab[fila:fila + eslora, col] = '0'
                    eslora3.append(current_pos)

                # Orientación 'O'este
                elif orient == 'O' and 0 <= col - eslora < 0 and '0' not in coors_posiO:
                    self.tab[fila, col: col - eslora: -1] = '0'
                    eslora3.append(current_pos)

            if len(eslora4) < 1:
                eslora = 4
                # Recogemos las 4 posiciones colindantes a 'current_pos'
                coors_posiN = self.tab[fila:fila - eslora:-1, col]
                coors_posiE = self.tab[fila, col: col + eslora]
                coors_posiS = self.tab[fila:fila + eslora, col]
                coors_posiO = self.tab[fila, col: col - eslora: -1]

                # Orientación 'N'orte:
                if orient == 'N' and 0 <= fila - eslora < 10 and '0' not in coors_posiN:
                    self.tab[fila:fila - eslora: -1, col] = '0'
                    eslora4.append(current_pos)  # hay que buscar la manera de añadirlos a una lista,diccionario...

                # Orientación 'E'ste:
                elif orient == 'E' and 0 <= col + eslora < 10 and '0' not in coors_posiE:
                    self.tab[fila, col: col + eslora] = '0'
                    eslora4.append(current_pos)

                # Orientación 'S'ur:
                elif orient == 'S' and 0 <= fila + eslora < 10 and '0' not in coors_posiS:
                    self.tab[fila:fila + eslora, col] = '0'
                    eslora4.append(current_pos)

                # Orientación 'O'este
                elif orient == 'O' and 0 <= col - eslora < 0 and '0' not in coors_posiO:
                    self.tab[fila, col: col - eslora: -1] = '0'
                    eslora4.append(current_pos)


            else:
                break



    def user_hit_or_not(self, long, lati): #this function changes the User Shoot Zone
        if self.tab[long, lati] == "0":
            self.tab2[long, lati] = "X"
            return True
        else:
            self.tab2[long, lati] = "_"
            return False

    def machine_hit_or_not(self, long, lati): #this function shows the shoots of the machine on the user's boat board
        if self.tab[long, lati] == "0":
            self.tab[long, lati] = "X"
            return True
        else:
            self.tab[long, lati] = "_"
            return False
