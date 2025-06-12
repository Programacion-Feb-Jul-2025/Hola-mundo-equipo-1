class JuegoGatoConsola:
    def __init__(self):
        self.jugador_x = input("Nombre del Jugador X: ") or "Jugador X"
        self.jugador_o = input("Nombre del Jugador O: ") or "Jugador O"
        self.turno = "X"
        self.tablero = [[" " for _ in range(3)] for _ in range(3)]
        self.historial = {"X": 0, "O": 0, "Empates": 0}

    def mostrar_tablero(self):
        print("\n  0   1   2")
        for i, fila in enumerate(self.tablero):
            print(i, " | ".join(fila))
            if i < 2:
                print("  ---------")
        print()

    def cambiar_turno(self):
        self.turno = "O" if self.turno == "X" else "X"

    def movimiento_valido(self, fila, col):
        return 0 <= fila < 3 and 0 <= col < 3 and self.tablero[fila][col] == " "

    def verificar_ganador(self, simbolo):
        for i in range(3):
            if all(self.tablero[i][j] == simbolo for j in range(3)) or \
               all(self.tablero[j][i] == simbolo for j in range(3)):
                return True
        if all(self.tablero[i][i] == simbolo for i in range(3)) or \
           all(self.tablero[i][2 - i] == simbolo for i in range(3)):
            return True
        return False

    def tablero_lleno(self):
        return all(celda != " " for fila in self.tablero for celda in fila)

    def reiniciar_tablero(self):
        self.tablero = [[" " for _ in range(3)] for _ in range(3)]
        self.turno = "X"

    def jugar_turno(self):
        jugador = self.jugador_x if self.turno == "X" else self.jugador_o
        while True:
            try:
                entrada = input(f"{jugador} ({self.turno}), ingresa fila y columna (ej. 0 1): ")
                fila, col = map(int, entrada.strip().split())
                if self.movimiento_valido(fila, col):
                    self.tablero[fila][col] = self.turno
                    break
                else:
                    print("Movimiento invalido. Intenta de nuevo.")
            except (ValueError, IndexError):
                print("Entrada invalida. Usa dos numeros separados por espacio (0-2).")

    def jugar(self):
        while True:
            self.mostrar_tablero()
            self.jugar_turno()
            if self.verificar_ganador(self.turno):
                ganador = self.jugador_x if self.turno == "X" else self.jugador_o
                print(f"\n¡{ganador} ({self.turno}) gana!\n")
                self.historial[self.turno] += 1
                self.mostrar_historial()
                if not self.preguntar_reinicio():
                    break
                self.reiniciar_tablero()
            elif self.tablero_lleno():
                print("\n¡Empate!\n")
                self.historial["Empates"] += 1
                self.mostrar_historial()
                if not self.preguntar_reinicio():
                    break
                self.reiniciar_tablero()
            else:
                self.cambia
