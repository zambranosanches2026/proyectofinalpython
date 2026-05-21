# Programa Python en Repositorio
import tkinter as tk

ventana = tk.Tk()
ventana.title("Programa para subir a Repositorio")
ventana.geometry("400x250")
ventana.configure(bg="#1e1e2f")  # Fondo oscuro moderno

# Fuente personalizada (familia, tamaño, estilo)
fuente = ("Arial", 18, "bold")

etiqueta = tk.Label(
    ventana,
    text="Este Programa es de Gera Aguilar",
    font=fuente,
    fg="#00ffcc",        # Color del texto (turquesa brillante)
    bg="#1e1e2f",        # Fondo igual al de la ventana
    wraplength=350,      # Ajuste de texto automático
    justify="center"
)

etiqueta.pack(pady=60)

ventana.mainloop()