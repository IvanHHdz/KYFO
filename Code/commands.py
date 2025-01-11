import os
from format import color
import re

# * List Elements
def le(arg1 = None):
    if arg1:
        if re.match(r"^\./.+", arg1):
            rute = re.sub(r"^\.", f"{gr()}", arg1)
        else:
            print(color("Red", "Invalid Rute!"))
            return
    else:
        rute = gr()
    for item in os.listdir(rute):
        c_rute = os.path.join(rute, item)
        if os.path.isfile(c_rute):
            print(color('Blue', item))
        elif os.path.isdir(c_rute):
            print(color('Yellow', item))

# * Show Tree
def st():
    pass

# * Get Rute 
def gr():
    return os.getcwd()

# * Show Rute
def sr():
    print(gr())

# * Commands
def command(command):
    commands = {
        "gr" : gr,
        "sr" : sr,
        "le" : le,
        "tr" : st
    }
    try:
        if len(command) == 1:
            return commands[command[0]]()
        else:
            return commands[command[0]](arg1 = command[1])
    except:
        print(color("Rojo", "Sintax Error!"))

def main():
    usr = "le Code".split(' ')
    command(usr)

if __name__ == "__main__":
    main()
