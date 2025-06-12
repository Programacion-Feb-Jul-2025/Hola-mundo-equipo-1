class Jugador:
    def __init__(self, simbolo, nombre):
        self.simbolo = simbolo
        self.nombre = nombre
        self.victorias = 0

class Tablero:
    def __init__(self):
        self.grid = [[" " for _ in range(3)] for _ in range(3)]

    def mostrar(self):
        print("\n  0   1   2")
        for i, fila in enumerate(self.grid):
            print(i, " | ".join(fila))
            if i < 2:
                print("  ---------")
        print()

    def colocar(self, fila, col, simbolo):
        self.grid[fila][col] = simbolo

    def esta_lleno(self):
        return all(c != " " for fila in self.grid for c in fila)

    def movimiento_valido(self, fila, col):
        return 0 <= fila < 3 and 0 <= col < 3 and self.grid[fila][col] == " "

    def verificar_ganador(self, simbolo):
        for i in range(3):
            if all(self.grid[i][j] == simbolo for j in range(3)):
                return True
            if all(self.grid[j][i] == simbolo for j in range(3)):
                return True
        if all(self.grid[i][i] == simbolo for i in range(3)):
            return True
        if all(self.grid[i][2 - i] == simbolo for i in range(3)):
            return True
        return False

    def reiniciar(self):
        self.grid = [[" " for _ in range(3)] for _ in range(3)]

class JuegoGato:
    def __init__(self):
        nombre_x = input("Nombre del Jugador X: ") or "Jugador X"
        nombre_o = input("Nombre del Jugador O: ") or "Jugador O"
        self.jugador_x = Jugador("X", nombre_x)
        self.jugador_o = Jugador("O", nombre_o)
        self.turno = self.jugador_x
        self.tablero = Tablero()
        self.empates = 0

    def cambiar_turno(self):
        self.turno = self.jugador_o if self.turno == self.jugador_x else self.jugador_x

    def jugar_turno(self):
        while True:
            try:
                entrada = input(f"{self.turno.nombre} ({self.turno.simbolo}), ingresa fila y columna: ")
                fila, col = map(int, entrada.strip().split())
                if self.tablero.movimiento_valido(fila, col):
                    self.tablero.colocar(fila, col, self.turno.simbolo)
                    break
                else:
                    print("Movimiento invalido.")
            except:
                print("Entrada invalida.")

    def mostrar_historial(self):
        print(f"{self.jugador_x.nombre} (X): {self.jugador_x.victorias}  |  {self.jugador_o.nombre} (O): {self.jugador_o.victorias}  |  Empates: {self.empates}\n")

    def preguntar_reinicio(self):
        r = input("Jugar otra vez? (s/n): ").lower()
        return r == "s"

    def jugar(self):
        while True:
            self.tablero.mostrar()
            self.jugar_turno()
            if self.tablero.verificar_ganador(self.turno.simbolo):
                print(f"\n{self.turno.nombre} ({self.turno.simbolo}) gana!\n")
                self.turno.victorias += 1
                self.mostrar_historial()
                if not self.preguntar_reinicio():
                    break
                self.tablero.reiniciar()
                self.turno = self.jugador_x
            elif self.tablero.esta_lleno():
                print("\nEmpate\n")
                self.empates += 1
                self.mostrar_historial()
                if not self.preguntar_reinicio():
                    break
                self.tablero.reiniciar()
                self.turno = self.jugador_x
            else:
                self.cambiar_turno()

if __name__ == "__main__":
    juego = JuegoGato()
    juego.jugar()

