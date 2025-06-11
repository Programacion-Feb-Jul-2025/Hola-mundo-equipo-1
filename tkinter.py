import tkinter as tk
class HolaMundoApp:
    def __init__(self, root):
        self.root=root
        self.root.title("Hola Mundo xd")
        self.root.geometry("300x100")
        self.etiqueta=tk.Label(self.root, text="Hola Mundo!")
        self.etiqueta.pack(pady=20)
        self.boton_salir=tk.Button(self.root, text="Salir", command=self.root.quit)
        self.boton_salir.pack()
if __name__ == "__main__":
    ventana=tk.Tk()
    app=HolaMundoApp(ventana)
    ventana.mainloop()
