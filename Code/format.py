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

def main():
    pass

if __name__ == "__main__":
    main()