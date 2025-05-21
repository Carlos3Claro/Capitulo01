import tkinter as tk
from tkinter import ttk

class Principal:
    def __init__(self, master):
        self.master = master
        master.title("El mundo de las bases de datos")

        self.label = tk.Label(master, text="El mundo de las bases de datos", font=("Arial", 24))
        self.label.pack(pady=10)

        self.descripcion = tk.Text(master, height=10, width=50)
        self.descripcion.pack(pady=10)

        self.menu_frame = tk.Frame(master)
        self.menu_frame.pack(side=tk.LEFT, padx=10)

        self.menu_button = ttk.Button(self.menu_frame, text="Menu", command=self.toggle_menu)
        self.menu_button.pack(pady=5)

        self.menu_visible = False
        self.botones_frame = tk.Frame(self.menu_frame)

        self.bd_relacional_button = ttk.Button(self.botones_frame, text="BD Relacional", command=self.ir_a_bd_relacional)
        self.bd_relacional_button.pack(pady=5)

        self.bd_no_relacional_button = ttk.Button(self.botones_frame, text="BD no Relacional", command=self.ir_a_bd_no_relacional)
        self.bd_no_relacional_button.pack(pady=5)

        self.planillas_button = ttk.Button(self.botones_frame, text="Planillas", command=self.ir_a_planillas)
        self.planillas_button.pack(pady=5)

    def toggle_menu(self):
        if self.menu_visible:
            self.botones_frame.pack_forget()
            self.menu_visible = False
        else:
            self.botones_frame.pack()
            self.menu_visible = True

    def ir_a_bd_relacional(self):
        print("Ir a BD Relacional")

    def ir_a_bd_no_relacional(self):
        print("Ir a BD no Relacional")

    def ir_a_planillas(self):
        print("Ir a Planillas")

root = tk.Tk()
principal = Principal(root)
root.mainloop()