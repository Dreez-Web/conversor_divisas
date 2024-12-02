import requests 
import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox

def obtener_tasa(moneda_origen, moneda_destino):
    url = f"https://v6.exchangerate-api.com/v6/94a06650cd1ab9010ecab60f/latest/{moneda_origen}"
    respuesta = requests.get(url)
    datos = respuesta.json()
    return datos ['conversion_rates'][moneda_destino]

def convertir():
    try:
        cantidad = float(divisa_1.get())
        origen = moneda_origen.get()
        destino = moneda_destino.get()
        
        if origen == "Seleccionar" or destino == "Seleccionar":
            messagebox.showerror("Error","Selecciona ambas monedas.")
            return
        
        tasa = obtener_tasa(origen, destino)
        resultado = cantidad * tasa
        divisa_2.delete(0, tk.END)
        divisa_2.insert(0, f"{resultado:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Introduce una cantidad valida")

main = tk.Tk()
main.title("Conversor de divisas")
main.geometry("300x300")

fuente = tkFont.Font(family="Times New Roman", size=18)

tk.Label (main, text= "Conversor de divisas",font=fuente).pack(pady=10)

opciones = ['USD', 'EUR','JPY','GBP','CLP','ARS']
moneda_origen = tk.StringVar(main)
moneda_origen.set("Seleccionar")
menu_origen = tk.OptionMenu(main,moneda_origen, *opciones)
menu_origen.pack()

divisa_1 = tk.Entry(main)
divisa_1.pack(pady=5)

moneda_destino = tk.StringVar(main)
moneda_destino.set("Seleccionar")
menu_destino = tk.OptionMenu(main, moneda_destino, *opciones)
menu_destino.pack()

boton = tk.Button(main, text="Convertir",command=convertir)
boton.pack()

divisa_2 = tk.Entry(main)
divisa_2.pack(pady=5)


main.mainloop()