import tkinter as tk


def show_frame(frame):
    frame.tkraise()


def create_button_frame(master, text):
    frame = tk.Frame(master, bg='#7587c6')
    label = tk.Label(frame, text=text, font=("Arial", 18), bg='#465ca9', fg='#ffffff')
    label.pack(pady=30)
    back_button = tk.Button(frame, text="Volver", command=lambda: show_frame(main_frame), font=("Arial", 12),
                            bg='#465ca9', fg='#ffffff', padx=20, pady=5)
    back_button.pack(pady=10)
    return frame


def open_page(page_name):
    new_window = tk.Toplevel(app)
    new_window.title(page_name)
    new_window.geometry("600x500")
    new_window.configure(bg='#7587c6')

    label = tk.Label(new_window, text=f"Esta es la página {page_name}", font=("Arial", 14), bg='#7587c6', fg='#ffffff')
    label.pack(pady=30)

    back_button = tk.Button(new_window, text="Volver", command=new_window.destroy, font=("Arial", 12), bg='#465ca9',
                            fg='#ffffff', padx=20, pady=5)
    back_button.pack(pady=10)


app = tk.Tk()
app.title("Proyecto estadística")
app.geometry("600x500")
app.configure(bg='#7587c6')

main_frame = tk.Frame(app, bg='#5168b7')
main_frame.place(x=0, y=0, width=600, height=500)

title_label = tk.Label(main_frame, text="Proyecto estadística", font=("Arial", 20, "bold"), bg='#6377bf', fg='#ffffff')
title_label.pack(pady=20)

buttons = [
    ("Ventana 1", create_button_frame(app, "Esta es la ventana 1")),
    ("Ventana 2", create_button_frame(app, "Esta es la ventana 2")),
    ("Ventana 3", create_button_frame(app, "Esta es la ventana 3")),
    ("Ventana 4", create_button_frame(app, "Esta es la ventana 4"))
]

for text, frame in buttons:
    frame.place(x=0, y=0, width=600, height=500)
    button = tk.Button(main_frame, text=text, command=lambda f=frame: show_frame(f), font=("Arial", 12), bg='#4d4d4d',
                       fg='#ffffff', padx=20, pady=5)
    button.pack(fill=tk.X, padx=50, pady=10)

# Agregar los botones adicionales en cada ventana
for frame in buttons:
    for i in range(1, 8):
        btn = tk.Button(frame[1], text=f"Botón {i}", font=("Arial", 12), bg='#4d4d4d', fg='#ffffff', padx=20, pady=5,
                        command=lambda p=i: open_page(f"Página {p}"))
        btn.pack(pady=5)

# Crear ventanas adicionales
window2 = create_button_frame(app, "Esta es la ventana 2")
for i in range(1, 8):
    btn = tk.Button(window2, text=f"Botón {i}", font=("Arial", 12), bg='#4d4d4d', fg='#ffffff', padx=20, pady=5,
                    command=lambda p=i: open_page(f"Página {p}"))
    btn.pack(pady=5)

window3 = create_button_frame(app, "Esta es la ventana 3")
for i in range(1, 8):
    btn = tk.Button(window3, text=f"Botón {i}", font=("Arial", 12), bg='#4d4d4d', fg='#ffffff', padx=20, pady=5,
                    command=lambda p=i: open_page(f"Página {p}"))
    btn.pack(pady=5)

window4 = create_button_frame(app, "Esta es la ventana 4")
for i in range(1, 8):
    btn = tk.Button(window4, text=f"Botón {i}", font=("Arial", 12), bg='#4d4d4d', fg='#ffffff', padx=20, pady=5,
                    command=lambda p=i: open_page(f"Página {p}"))
    btn.pack(pady=5)

show_frame(main_frame)
app.mainloop()
