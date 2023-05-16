import tkinter as tk

def show_frame(frame):
    frame.tkraise()

def create_button_frame(master, text):
    frame = tk.Frame(master, bg='#7587c6')
    label = tk.Label(frame, text=text, font=("Arial", 18), bg='#465ca9', fg='#ffffff')
    label.pack(pady=30)
    back_button = tk.Button(frame, text="Volver", command=lambda: show_frame(main_frame), font=("Arial", 12), bg='#465ca9', fg='#ffffff', padx=20, pady=5)
    back_button.pack(pady=10)
    return frame

app = tk.Tk()
app.title("Proyecto estadística")
app.geometry("500x420")
app.configure(bg='#7587c6')

main_frame = tk.Frame(app, bg='#5168b7')
main_frame.place(x=0, y=0, width=500, height=500)

title_label = tk.Label(main_frame, text="Proyecto estadística", font=("Arial", 20, "bold"), bg='#6377bf', fg='#ffffff')
title_label.pack(pady=20)

buttons = [
    ("Ventana 1", create_button_frame(app, "Esta es la ventana 1")),
    ("Ventana 2", create_button_frame(app, "Esta es la ventana 2")),
    ("Ventana 3", create_button_frame(app, "Esta es la ventana 3")),
    ("Ventana 4", create_button_frame(app, "Esta es la ventana 4"))
]

for text, frame in buttons:
    frame.place(x=0, y=0, width=500, height=420)
    button = tk.Button(main_frame, text=text, command=lambda f=frame: show_frame(f), font=("Arial", 12), bg='#4d4d4d', fg='#ffffff', padx=20, pady=5)
    button.pack(fill=tk.X, padx=50, pady=10)

# Agregar los botones adicionales en cada ventana
for frame in buttons:
    frame[1].btn1 = tk.Button(frame[1], text="Botón 1", font=("Arial", 12), bg='#4d4d4d', fg='#ffffff', padx=20, pady=5)
    frame[1].btn1.pack(pady=5)
    frame[1].btn2 = tk.Button(frame[1], text="Botón 2", font=("Arial", 12), bg='#4d4d4d', fg='#ffffff', padx=20, pady=5)
    frame[1].btn2.pack(pady=5)
    frame[1].btn3 = tk.Button(frame[1], text="Botón 3", font=("Arial", 12), bg='#4d4d4d', fg='#ffffff', padx=20, pady=5)
    frame[1].btn3.pack(pady=5)

show_frame(main_frame)
app.mainloop()
