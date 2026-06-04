import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk # Necesita instalar pillow: pip install pillow
import os

# -------------------------
# FUNCIONES (pantallas vacías por ahora)
# -------------------------
def abrir_registro_productos():
    reg = tk.Toplevel()
    reg.title("Registro de Productos")
    reg.geometry("450x450")
    reg.resizable(False, False)

    # Colores
    COLOR_FONDO = "#1E1E1E"
    COLOR_TEXTO = "white"
    COLOR_ENTRADA = "#2D2D2D"
    COLOR_BOTON = "#28A745"

    reg.configure(bg=COLOR_FONDO)

    # Frame principal
    frame = tk.Frame(reg, bg=COLOR_FONDO)
    frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Título
    titulo = tk.Label(
        frame,
        text="REGISTRO DE PRODUCTOS",
        font=("Segoe UI", 16, "bold"),
        bg=COLOR_FONDO,
        fg=COLOR_TEXTO
    )
    titulo.pack(pady=(0, 20))

    # ID
    lbl_id = tk.Label(
        frame,
        text="ID del Producto",
        font=("Segoe UI", 11),
        bg=COLOR_FONDO,
        fg=COLOR_TEXTO
    )
    lbl_id.pack(anchor="w")

    txt_id = tk.Entry(
        frame,
        font=("Segoe UI", 11),
        bg=COLOR_ENTRADA,
        fg="white",
        insertbackground="white"
    )
    txt_id.pack(fill="x", pady=(0, 10))

    # Descripción
    lbl_desc = tk.Label(
        frame,
        text="Descripción",
        font=("Segoe UI", 11),
        bg=COLOR_FONDO,
        fg=COLOR_TEXTO
    )
    lbl_desc.pack(anchor="w")

    txt_desc = tk.Entry(
        frame,
        font=("Segoe UI", 11),
        bg=COLOR_ENTRADA,
        fg="white",
        insertbackground="white"
    )
    txt_desc.pack(fill="x", pady=(0, 10))

    # Precio
    lbl_precio = tk.Label(
        frame,
        text="Precio",
        font=("Segoe UI", 11),
        bg=COLOR_FONDO,
        fg=COLOR_TEXTO
    )
    lbl_precio.pack(anchor="w")

    txt_precio = tk.Entry(
        frame,
        font=("Segoe UI", 11),
        bg=COLOR_ENTRADA,
        fg="white",
        insertbackground="white"
    )
    txt_precio.pack(fill="x", pady=(0, 10))

    # Categoría
    lbl_categoria = tk.Label(
        frame,
        text="Categoría",
        font=("Segoe UI", 11),
        bg=COLOR_FONDO,
        fg=COLOR_TEXTO
    )
    lbl_categoria.pack(anchor="w")

    txt_categoria = tk.Entry(
        frame,
        font=("Segoe UI", 11),
        bg=COLOR_ENTRADA,
        fg="white",
        insertbackground="white"
    )
    txt_categoria.pack(fill="x", pady=(0, 20))

    # Función guardar
    def guardar_producto():

        id_prod = txt_id.get().strip()
        descripcion = txt_desc.get().strip()
        precio = txt_precio.get().strip()
        categoria = txt_categoria.get().strip()

        if not all([id_prod, descripcion, precio, categoria]):
            messagebox.showwarning(
                "Campos Vacíos",
                "Por favor complete todos los campos."
            )
            return

        try:
            float(precio)
        except ValueError:
            messagebox.showerror(
                "Error",
                "El precio debe ser un número."
            )
            return

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        archivo = os.path.join(BASE_DIR, "productos.txt")

        with open(archivo, "a", encoding="utf-8") as f:
            f.write(
                f"{id_prod}|{descripcion}|{precio}|{categoria}\n"
            )

        messagebox.showinfo(
            "Guardado",
            "Producto registrado correctamente."
        )

        txt_id.delete(0, tk.END)
        txt_desc.delete(0, tk.END)
        txt_precio.delete(0, tk.END)
        txt_categoria.delete(0, tk.END)

        txt_id.focus()

    # Botón
    btn_guardar = tk.Button(
        frame,
        text="💾 Guardar Producto",
        command=guardar_producto,
        bg=COLOR_BOTON,
        fg="white",
        font=("Segoe UI", 11, "bold"),
        padx=10,
        pady=8,
        cursor="hand2",
        relief="flat"
    )

    btn_guardar.pack(fill="x")

from datetime import datetime

def mostrar_ticket(producto, precio, cantidad, total):
  ticket = tk.Toplevel()
  ticket.title("Ticket de Venta")
  ticket.geometry("300x350")
  ticket.resizable(False, False)

  # Fecha y hora
  fecha_hora = datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")

  # Texto del ticket
  texto = (
  " *** PUNTO DE VENTA ***\n"
  "--------------------------------------\n"
  f"Fecha: {fecha_hora}\n"
  "--------------------------------------\n"
  f"Producto: {producto}\n"
  f"Precio: ${precio}\n"
  f"Cantidad: {cantidad}\n"
  "--------------------------------------\n"
  f"TOTAL: ${total}\n"
  "--------------------------------------\n"
  " ¡GRACIAS POR SU COMPRA!\n"
  )

  lbl_ticket = tk.Label(ticket, text=texto, justify="left", font=("Consolas", 11))
  lbl_ticket.pack(pady=15)

  btn_cerrar = ttk.Button(ticket, text="Cerrar", command=ticket.destroy)
  btn_cerrar.pack(pady=10)
         
def abrir_registro_ventas():
   ven = tk.Toplevel()
   ven.title("Registro de Ventas")
   ven.geometry("420x430")
   ven.resizable(False, False)
   # ------------------------------------
   # Cargar productos desde productos.txt
   # ------------------------------------
   productos = {}
   try:
      BASE_DIR = os.path.dirname(os.path.abspath(__file__))
      archivof = os.path.join(BASE_DIR,"productos.txt")
      with open(archivof, "r", encoding="utf-8") as archivo:
         for linea in archivo:
            partes = linea.strip().split("|")
            if len(partes) == 4:
               idp, desc, precio, cat = partes
               productos[desc] = float(precio)
   except FileNotFoundError:
      messagebox.showerror("Error", "No se encontró el archivo productos.txt")
      ven.destroy()
      return
  # Lista de nombres de productos
   lista_productos = list(productos.keys())
   # ------------------------------------
   # CONTROLES VISUALES
   # ------------------------------------
   lbl_prod = tk.Label(ven, text="Producto:", font=("Arial", 12))
   lbl_prod.pack(pady=5)
   cb_producto = ttk.Combobox(ven, values=lista_productos, font=("Arial", 12), state="readonly")
   cb_producto.pack(pady=5)
   lbl_precio = tk.Label(ven, text="Precio:", font=("Arial", 12))
   lbl_precio.pack(pady=5)
   txt_precio = tk.Entry(ven, font=("Arial", 12), state="readonly")
   txt_precio.pack(pady=5)
   lbl_cantidad = tk.Label(ven, text="Cantidad:", font=("Arial", 12))
   lbl_cantidad.pack(pady=5)
   cantidad_var = tk.StringVar(ven)
   ven.cantidad_var = cantidad_var   # importante: mantiene la referencia
   txt_cantidad = tk.Entry(ven, font=("Arial", 12), textvariable=cantidad_var)
   txt_cantidad.pack(pady=5)  
   cantidad_var.trace_add("write", lambda *args: calcular_total())
   lbl_total = tk.Label(ven, text="Total:", font=("Arial", 12))
   lbl_total.pack(pady=5)
   txt_total = tk.Entry(ven, font=("Arial", 12), state="readonly")
   txt_total.pack(pady=5)
   # ------------------------------------
   # FUNCIONES
   # ------------------------------------
   def actualizar_precio(event):      
      prod = cb_producto.get()
      if prod in productos:
         txt_precio.config(state="normal")
         txt_precio.delete(0, tk.END)
         txt_precio.insert(0, productos[prod])
         txt_precio.config(state="readonly")
         calcular_total()
   def calcular_total(*args):      
      try:
         cant = int(txt_cantidad.get())
         precio = float(txt_precio.get())
         total = cant * precio
         txt_total.config(state="normal")
         txt_total.delete(0, tk.END)
         txt_total.insert(0, total)
         txt_total.config(state="readonly")
      except:
         # Si no hay número válido, limpiar el total
         txt_total.config(state="normal")
         txt_total.delete(0, tk.END)
         txt_total.config(state="readonly")
   def registrar_venta():
      prod = cb_producto.get()
      precio = txt_precio.get()
      cant = txt_cantidad.get()
      total = txt_total.get()
      if prod == "" or precio == "" or cant == "" or total == "":
         messagebox.showwarning("Campos Vacíos", "Todos los campos deben estar completos.")
         return
      # Guardar venta
      BASE_DIR = os.path.dirname(os.path.abspath(__file__))
      archivov = os.path.join(BASE_DIR,"ventas.txt")
      with open(archivov, "a", encoding="utf-8") as archivo:
         archivo.write(f"{prod}|{precio}|{cant}|{total}\n")
         messagebox.showinfo("Venta Registrada", "La venta se registró correctamente.")
         mostrar_ticket(prod, precio, cant, total)
      # Limpiar campos
      cb_producto.set("")
      txt_precio.config(state="normal"); txt_precio.delete(0, tk.END); txt_precio.config(state="readonly")
      txt_cantidad.delete(0, tk.END)
      txt_total.config(state="normal"); txt_total.delete(0, tk.END); txt_total.config(state="readonly")
   # ------------------------------------
   # EVENTOS Y BOTÓN
   # ------------------------------------
   cb_producto.bind("<<ComboboxSelected>>", actualizar_precio)
   btn_guardar = ttk.Button(ven, text="Registrar Venta", command=registrar_venta)
   btn_guardar.pack(pady=25)
   
def abrir_reportes():
   messagebox.showinfo("Reportes", "Aquí irá el módulo de reportes.")

def abrir_acerca_de():
   messagebox.showinfo("Acerca de", "Punto de Venta de RopanProyecto Escolar\n Versión 1.0")


# -------------------------
# VENTANA PRINCIPAL
# -------------------------
# -------------------------
# VENTANA PRINCIPAL
# -------------------------
ventana = tk.Tk()
ventana.title("Punto de Venta - Ropa")
ventana.geometry("550x700")
ventana.resizable(False, False)

# Colores
COLOR_FONDO = "#1E1E1E"
COLOR_PANEL = "#252526"
COLOR_TEXTO = "#FFFFFF"

ventana.configure(bg=COLOR_FONDO)

# -------------------------
# ENCABEZADO
# -------------------------
frame_encabezado = tk.Frame(
    ventana,
    bg=COLOR_PANEL
)
frame_encabezado.pack(fill="x")

lbl_titulo = tk.Label(
    frame_encabezado,
    text="PUNTO DE VENTA",
    font=("Segoe UI", 22, "bold"),
    bg=COLOR_PANEL,
    fg="white"
)

lbl_titulo.pack(pady=(20, 5))

lbl_subtitulo = tk.Label(
    frame_encabezado,
    text="Sistema de Administración de Ropa",
    font=("Segoe UI", 11),
    bg=COLOR_PANEL,
    fg="#CCCCCC"
)

lbl_subtitulo.pack(pady=(0, 15))

# -------------------------
# LOGO
# -------------------------
try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    imagen = Image.open(
        os.path.join(BASE_DIR, "logo.png")
    )

    imagen = imagen.resize((220, 220))

    img_logo = ImageTk.PhotoImage(imagen)

    lbl_logo = tk.Label(
        ventana,
        image=img_logo,
        bg=COLOR_FONDO
    )

    lbl_logo.pack(pady=20)

except:

    lbl_sin_logo = tk.Label(
        ventana,
        text="LOGO DEL SISTEMA",
        font=("Segoe UI", 14, "bold"),
        bg=COLOR_FONDO,
        fg="white"
    )

    lbl_sin_logo.pack(pady=40)

# -------------------------
# CONTENEDOR DE BOTONES
# -------------------------
frame_botones = tk.Frame(
    ventana,
    bg=COLOR_FONDO
)

frame_botones.pack(pady=10)

# Botón Registro Productos
btn_reg_prod = tk.Button(
    frame_botones,
    text="📦 Registro de Productos",
    command=abrir_registro_productos,
    bg="#0078D7",
    fg="white",
    font=("Segoe UI", 12, "bold"),
    relief="flat",
    cursor="hand2",
    width=25,
    pady=10
)

btn_reg_prod.pack(pady=8)

# Botón Ventas
btn_reg_ventas = tk.Button(
    frame_botones,
    text="💰 Registro de Ventas",
    command=abrir_registro_ventas,
    bg="#28A745",
    fg="white",
    font=("Segoe UI", 12, "bold"),
    relief="flat",
    cursor="hand2",
    width=25,
    pady=10
)

btn_reg_ventas.pack(pady=8)

# Botón Reportes
btn_reportes = tk.Button(
    frame_botones,
    text="📊 Reportes",
    command=abrir_reportes,
    bg="#FFC107",
    fg="black",
    font=("Segoe UI", 12, "bold"),
    relief="flat",
    cursor="hand2",
    width=25,
    pady=10
)

btn_reportes.pack(pady=8)

# Botón Acerca de
btn_acerca = tk.Button(
    frame_botones,
    text="ℹ️ Acerca de",
    command=abrir_acerca_de,
    bg="#6C757D",
    fg="white",
    font=("Segoe UI", 12, "bold"),
    relief="flat",
    cursor="hand2",
    width=25,
    pady=10
)

btn_acerca.pack(pady=8)

# -------------------------
# PIE DE PÁGINA
# -------------------------
lbl_version = tk.Label(
    ventana,
    text="Versión 1.0 | MQ Académico",
    font=("Segoe UI", 9),
    bg=COLOR_FONDO,
    fg="#AAAAAA"
)

lbl_version.pack(side="bottom", pady=15)

# -------------------------
# INICIAR APP
# -------------------------
ventana.mainloop()