import keyboard

archivo = open("archivo.txt", "a")

def eventokey(evento):
    archivo.write(evento.name + " ")
    print(f"Escribiste: {evento.name}")

keyboard.on_press(eventokey)
keyboard.wait("esc")

archivo.close()