
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('💲💲💲 National Bank of Ukraine 💲💲💲')
window.geometry('500x210')

def dolar():
    griwna = user_text.get()
    messagebox.showinfo('message', f"It's Dolar {float(griwna)* 0.028}")
def euro():
    griwna = user_text.get()
    messagebox.showinfo('message', f"It's Euro {float(griwna)* 0.025}")
def kopiyki():
    griwna = user_text.get()
    messagebox.showinfo('message', f"It's Kopiyki {float(griwna)* 100}")

frame = tk.Frame(window, padx=10, pady=10)
frame.pack(pady=20)
tk.Label(frame, text='Enter Many(Griwni)').grid(row=0, column=0)
user_text = tk.Entry(frame, font=('Verdana', 15, 'bold'))
user_text.grid(row=0, column=1)

tk.Button(frame, text='Dolar', pady=10, padx=20, command=dolar).grid(row=1, columnspan=2)
tk.Button(frame, text='Euro', pady=10, padx=20, command=euro).grid(row=2, columnspan=2)
tk.Button(frame, text='Kopiyki', pady=10, padx=20, command=kopiyki).grid(row=3, columnspan=2)

window.mainloop()
