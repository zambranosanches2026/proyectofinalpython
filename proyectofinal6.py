import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# -------------------------
# FUNCIONES
# -------------------------
def abrir_registro_productos():

    reg = tk.Toplevel()
    reg.title("Registro de Productos")
    reg.geometry("500x500")
    reg.configure(bg="#f4f6f9")
    reg.resizable(False, False)

    # -------------------------
    # TÍTULO
    # -------------------------
    titulo = tk.Label(
        reg,
        text="Registro de Productos",
        font=("Arial", 20, "bold"),
        bg="#f4f6f9",
        fg="#1f2937"
    )
    titulo.pack(pady=20)

    # -------------------------
    # FRAME PRINCIPAL
    # -------------------------
    frame = tk.Frame(
        reg,
        bg="white",
        bd=2,
        relief="groove"
    )
    frame.pack(padx=30, pady=10, fill="both", expand=True)

    # -------------------------
    # ESTILO
    # -------------------------
    label_style = {
        "font": ("Arial", 11, "bold"),
        "bg": "white",
        "fg": "#374151",
        "anchor": "w"
    }

    entry_style = {
        "font": ("Arial", 11),
        "bd": 1,
        "relief": "solid",
        "width": 30
    }

    # -------------------------
    # CAMPOS
    # -------------------------
    tk.Label(frame, text="ID del Producto", **label_style).pack(pady=(20,5), padx=30, fill="x")
    txt_id = tk.Entry(frame, **entry_style)
    txt_id.pack(pady=5)

    tk.Label(frame, text="Descripción", **label_style).pack(pady=(15,5), padx=30, fill="x")
    txt_desc = tk.Entry(frame, **entry_style)
    txt_desc.pack(pady=5)

    tk.Label(frame, text="Precio", **label_style).pack(pady=(15,5), padx=30, fill="x")
    txt_precio = tk.Entry(frame, **entry_style)
    txt_precio.pack(pady=5)

    tk.Label(frame, text="Categoría", **label_style).pack(pady=(15,5), padx=30, fill="x")
    txt_categoria = tk.Entry(frame, **entry_style)
    txt_categoria.pack(pady=5)

    # -------------------------
    # FUNCIÓN GUARDAR
    # -------------------------
    def guardar_producto():

        id_prod = txt_id.get().strip()
        descripcion = txt_desc.get().strip()
        precio = txt_precio.get().strip()
        categoria = txt_categoria.get().strip()

        # Validaciones
        if id_prod == "" or descripcion == "" or precio == "" or categoria == "":
            messagebox.showwarning(
                "Campos Vacíos",
                "Por favor complete todos los campos."
            )
            return

        # Validar precio
        try:
            float(precio)
        except:
            messagebox.showerror(
                "Error",
                "El precio debe ser un número."
            )
            return

        # Guardar archivo
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        archivo = os.path.join(BASE_DIR, "productos.txt")

        with open(archivo, "a", encoding="utf-8") as archivo:
            archivo.write(f"{id_prod}|{descripcion}|{precio}|{categoria}\n")

        messagebox.showinfo(
            "Guardado",
            "Producto registrado correctamente."
        )

        # Limpiar campos
        txt_id.delete(0, tk.END)
        txt_desc.delete(0, tk.END)
        txt_precio.delete(0, tk.END)
        txt_categoria.delete(0, tk.END)

    # -------------------------
    # BOTÓN GUARDAR
    # -------------------------
    btn_guardar = tk.Button(
        frame,
        text="Guardar Producto",
        command=guardar_producto,
        font=("Arial", 12, "bold"),
        bg="#111827",
        fg="white",
        activebackground="#374151",
        activeforeground="white",
        width=20,
        height=2,
        cursor="hand2",
        relief="flat"
    )

    btn_guardar.pack(pady=30)


# -------------------------
# FUNCIONES RESTANTES
# -------------------------
def abrir_registro_ventas():
    messagebox.showinfo("Registro de Ventas", "Aquí irá el módulo de ventas.")

def abrir_reportes():
    messagebox.showinfo("Reportes", "Aquí irá el módulo de reportes.")

def abrir_acerca_de():
    messagebox.showinfo(
        "Acerca de",
        "Punto de Venta de Ropa\nProyecto Escolar\nVersión 1.0"
    )

# -------------------------
# VENTANA PRINCIPAL
# -------------------------
ventana = tk.Tk()
ventana.title("Punto de Venta")
ventana.geometry("500x650")
ventana.configure(bg="#f4f6f9")
ventana.resizable(False, False)

# -------------------------
# LOGO
# -------------------------
try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    imagen = Image.open(os.path.join(BASE_DIR, "logo.png"))
    imagen = imagen.resize((220, 220))

    img_logo = ImageTk.PhotoImage(imagen)

    lbl_logo = tk.Label(
        ventana,
        image=img_logo,
        bg="#f4f6f9"
    )
    lbl_logo.pack(pady=20)

except:
    lbl_sin_logo = tk.Label(
        ventana,
        text="(Aquí va el logo del sistema)",
        font=("Arial", 14),
        bg="#f4f6f9"
    )
    lbl_sin_logo.pack(pady=40)

# -------------------------
# TÍTULO
# -------------------------
titulo_principal = tk.Label(
    ventana,
    text="Sistema Punto de Venta",
    font=("Arial", 22, "bold"),
    bg="#f4f6f9",
    fg="#111827"
)

titulo_principal.pack(pady=10)

# -------------------------
# ESTILO BOTONES
# -------------------------
btn_config = {
    "bg": "#111827",
    "fg": "white",
    "font": ("Arial", 12, "bold"),
    "width": 25,
    "height": 2,
    "cursor": "hand2",
    "relief": "flat",
    "activebackground": "#374151",
    "activeforeground": "white"
}

# -------------------------
# BOTONES PRINCIPALES
# -------------------------
btn_reg_prod = tk.Button(
    ventana,
    text="Registro de Productos",
    command=abrir_registro_productos,
    **btn_config
)
btn_reg_prod.pack(pady=10)

btn_reg_ventas = tk.Button(
    ventana,
    text="Registro de Ventas",
    command=abrir_registro_ventas,
    **btn_config
)
btn_reg_ventas.pack(pady=10)

btn_reportes = tk.Button(
    ventana,
    text="Reportes",
    command=abrir_reportes,
    **btn_config
)
btn_reportes.pack(pady=10)

btn_acerca = tk.Button(
    ventana,
    text="Acerca de",
    command=abrir_acerca_de,
    **btn_config
)
btn_acerca.pack(pady=10)

# -------------------------
# INICIAR APP
# -------------------------
ventana.mainloop()