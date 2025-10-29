import tkinter as tk

ventana = tk.Tk()
ventana.title("tiktok")
ventana.geometry("600x500")
ventana.resizable(False,False)

def home():
    home =tk.Tk()
    home.title('home')
    home.geometry("600x500")

    Bienvenida =tk.Label(home,text="!Inicio secion exitoso¡,Bienvenido a Tiktok donde podras visualizar lo que te guste",bg="yellow")
    Bienvenida.pack()

cuadro = tk.Frame(ventana, bg="pink", bd=4, relief="ridge")
cuadro.pack(pady=40, padx=20, fill="both", expand=True)

titulo_tikok = tk.Label(cuadro, text= "Bienvenido/a a tiktok", font= "Arial", bg= "pink")
titulo_tikok.pack(pady=10)

etiqueta_nombre = tk.Label(cuadro, text="Ingresa tu usuario:", bg= "pink")
etiqueta_nombre.pack(pady=5)
entrada_nombre = tk.Entry(cuadro)
entrada_nombre.pack(pady=5)

etiqueta_contrasena= tk.Label(cuadro, text="Ingresa tu contraseña:", bg= "pink")
etiqueta_contrasena.pack(pady=5)
entrada_contrasena = tk.Entry(cuadro)
entrada_contrasena.pack(pady=5)

usuario_correcto = "micaelita"
contrasena_correcta = "2222"

def iniciar_sesion():
    nombre_usuario = entrada_nombre.get()
    contrasena = entrada_contrasena.get()
    if nombre_usuario == usuario_correcto and contrasena == contrasena_correcta:
        ventana.destroy()
        home()
    else:
        saludo.config(text=f"¡Inicio de sesion incorrecto!", fg="red")
        
def salir():
    ventana.destroy()


boton = tk.Button(cuadro, text="Confirmar",bg= "green",  command=iniciar_sesion)
boton.pack(pady=10)

bt_salir = tk.Button(cuadro, text="Salir", bg="red", command=salir)
bt_salir.pack()

saludo = tk.Label(cuadro, text="", bg= "violet")
saludo.pack()

ventana.mainloop()