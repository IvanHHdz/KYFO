import os

RUTE = os.getcwd()

def color(color, text):
    if type(color) == int:
        return f"\033[{color}m{text}\033[0m"
    elif type(color) == str:
        colors = {
            "Negro"     :   30,
            "Rojo"      :   31,
            "Verde"     :   32,
            "Amarillo"  :   33,
            "Azul"      :   34,
            "Magenta"   :   35,
            "Cian"      :   36,
            "Blanco"    :   37
        }
        return f"\033[{colors[color]}m{text}\033[0m"
    else:
        pass

def ls():
    for item in os.listdir():
        ruta_completa = os.path.join(RUTE, item)
        if os.path.isfile(ruta_completa):
            print(color())
        elif os.path.isdir(ruta_completa):
            print(f"\033[31m{item}\033[0m")

def main():
    commands = {
        "ls" : ls
    }
    #commands["ls"]
    print(color("Amarillo", "Hola"))

if __name__ == "__main__":
    main()