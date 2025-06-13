import tkinter as tk
from tkinter import simpledialog, messagebox

class JuegoGato:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de Gato")

        self.jugador_x = simpledialog.askstring("Jugador X", "Nombre del Jugador X:")
        self.jugador_o = simpledialog.askstring("Jugador O", "Nombre del Jugador O:")
        if not self.jugador_x: self.jugador_x = "Jugador X"
        if not self.jugador_o: self.jugador_o = "Jugador O"

        self.turno = "X"
        self.historial = {"X": 0, "O": 0, "Empates": 0}
        self.botones = [[None for _ in range(3)] for _ in range(3)]

        self.label_turno = tk.Label(self.root, text="", font=("Arial", 16))
        self.label_turno.grid(row=3, column=0, columnspan=3)

        self.label_historial = tk.Label(self.root, text="", font=("Arial", 12))
        self.label_historial.grid(row=4, column=0, columnspan=3)

      
        self.boton_reglas = tk.Button(self.root, text="Reglas del Juego", font=("Arial", 10), command=self.mostrar_reglas)
        self.boton_reglas.grid(row=5, column=0, columnspan=3, pady=10)

        self.crear_tablero()
        self.actualizar_info()

    def crear_tablero(self):
        for fila in range(3):
            for col in range(3):
                boton = tk.Button(self.root, text=" ", width=10, height=4,
                                  font=("Arial", 24), command=lambda f=fila, c=col: self.click(f, c))
                boton.grid(row=fila, column=col)
                self.botones[fila][col] = boton

    def click(self, fila, col):
        boton = self.botones[fila][col]
        if boton["text"] == " ":
            boton["text"] = self.turno
            if self.verificar_ganador(self.turno):
                nombre_ganador = self.jugador_x if self.turno == "X" else self.jugador_o
                messagebox.showinfo("Ganador", f"{nombre_ganador} gana")
                self.historial[self.turno] += 1
                self.reiniciar_juego()
            elif self.tablero_lleno():
                messagebox.showinfo("Empate", "Empate")
                self.historial["Empates"] += 1
                self.reiniciar_juego()
            else:
                self.turno = "O" if self.turno == "X" else "X"
                self.actualizar_info()

    def verificar_ganador(self, simbolo):
        for i in range(3):
            if all(self.botones[i][j]["text"] == simbolo for j in range(3)) or \
               all(self.botones[j][i]["text"] == simbolo for j in range(3)):
                return True
        if all(self.botones[i][i]["text"] == simbolo for i in range(3)) or \
           all(self.botones[i][2 - i]["text"] == simbolo for i in range(3)):
            return True
        return False

    def tablero_lleno(self):
        return all(self.botones[f][c]["text"] != " " for f in range(3) for c in range(3))

    def reiniciar_juego(self):
        for fila in self.botones:
            for boton in fila:
                boton["text"] = " "
        self.turno = "X"
        self.actualizar_info()

    def actualizar_info(self):
        jugador = self.jugador_x if self.turno == "X" else self.jugador_o
        self.label_turno.config(text=f"Turno: {jugador} ({self.turno})")
        self.label_historial.config(
            text=f"{self.jugador_x} (X): {self.historial['X']}  |  {self.jugador_o} (O): {self.historial['O']}  |  Empates: {self.historial['Empates']}"
        )

    def mostrar_reglas(self):
        reglas = (
            "Reglas del Juego de Gato (Tres en linea):\n\n"
            "1. Dos jugadores participan, uno con 'X' y otro con 'O'.\n" 
            "2. El objetivo es alinear tres simbolos iguales (X o O) en linea recta.\n"
            "   Esto puede ser en horizontal, vertical o diagonal.\n"
            "3. Los jugadores alternan turnos haciendo clic en las casillas vacias.\n"
            "4. Gana el jugador que primero forme una linea de tres simbolos.\n"
            "5. Si todas las casillas se llenan sin que nadie gane, es un empate."
        )
        messagebox.showinfo("Reglas del Juego", reglas)

if __name__ == "__main__":
    root = tk.Tk()
    juego = JuegoGato(root)
    root.mainloop()


