def color(color, text):
    if type(color) == int:
        return f"\033[{color}m{text}\033[0m"
    elif type(color) == str:
        colors = {
            "Black"     :   30,
            "Red"      :   31,
            "Green"     :   32,
            "Yellow"  :   33,
            "Blue"      :   34,
            "Magenta"   :   35,
            "Cyan"      :   36,
            "White"    :   37
        }
        return f"\033[{colors[color]}m{text}\033[0m"
    else:
        color = [str(c) for c in color]
        return f"\033[38;2;{';'.join(color)}m{text}\033[0m"

def p_error(msg):
    print(color("Red", msg))
    
def p_color(msg, c):
    if type(msg) == str:
        print(color(c, msg))
    else:
        for i in range(len(msg)):
            print(color(c[i], msg[i]),end="")
        print()

def p_elemets(l, c1, c2):
    for i in range(len(l[0])):
        p_color(l[0][i], c1 if l[1][i] else c2)

def main():
    pass

if __name__ == "__main__":
    main()