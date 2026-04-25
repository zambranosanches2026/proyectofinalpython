#programa para el repositorio
import tkinter as Tk

# Crear la ventana
ventana = Tk.Tk()
ventana.title("Programa para subir a repositorio")
ventana.geometry("500x300")  # un poco más grande

# Cambiar el fondo de la ventana
ventana.configure(bg="#1e1e2f")  # un fondo oscuro elegante

# Crear la etiqueta con estilo
etiqueta = Tk.Label(
    ventana,
    text="Este programa es de Rafael Zambrano y Luis Sánchez",
    font=("Arial", 16, "bold"),   # Fuente grande y negrita
    fg="#FFD700",                  # Color del texto (dorado)
    bg="#1e1e2f",                  # Fondo de la etiqueta igual que la ventana
    padx=10, pady=10
)
etiqueta.pack(pady=50)

# Ejecutar la ventana
ventana.mainloop()