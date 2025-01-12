import os
from format import color, p_error, p_elemets, p_color
import re
from functools import partial

# * Get Elements
def ge(rute):
    e = [[],[]]
    for item in os.listdir(rute):
        c_rute = os.path.join(rute, item)
        if os.path.isdir(c_rute):
            e[1].append(True)
        else:
            e[1].append(False)
        e[0].append(item)
    return e

# * Verication of Arguments - Rute
def ver_arg_rut(rute):
    if rute:
        if re.match(r"^\./.+", rute):
            return re.sub(r"^\.", f"{gr()}", rute)
        elif re.match(r"^[\w/ \.-]*/.+", rute):
            return rute
        else:
            p_error('Invalid Rute')
    return gr()
    

# * List Elements
def le(arg1 = None):
    rute = ver_arg_rut(arg1)
    p_elemets(ge(rute), "Cyan", "Magenta")

# * Get Rute 
def gr():
    return os.getcwd()

# * Show Tree
def st(arg1=None, t=1):
    rute = ver_arg_rut(arg1)
    ele = ge(rute)
    if t == 1:
        p_color(rute, "Cyan")
    for i in range(len(ele[0])):
        if ele[1][i]:
            p_color(['|\t'*(t-1)+'|-> ',ele[0][i]],['Yellow','Cyan'])
            st(rute+"/"+ele[0][i], t+1)

# * Show Rute
def sr():
    print(gr())

# * Documentation
def dc(arg1=None,st = False):
    if st:
        p_error("Try 'st' to see the documentation.")
    else:
        if arg1:
            pass
        else:
            print("Valid commands:")
            p = partial(p_color, c=["Green","White"])
            p(["\tsr" , " - Show actual rute."])
            p(["\tle <rute>"," - List the elements of a rute, the actual rute by default."])
            p(["\tdc"," - Show the documentation."])
            p(["\tst <rute>", " - Show a tree of directories from a rute, the actual rute by default."])
    #TODO agregar la documentacion

# * Commands
def command(command):
    commands = {
        "sr" : sr,
        "le" : le,
        "dc" : dc,
        "st" : st
    }
    try:
        if len(command) == 1:
            return commands[command[0]]()
        else:
            return commands[command[0]](arg1 = command[1])
    except:
        p_error("Sintax Error")
        dc(st = True)

def main():
    dc()
    st()

if __name__ == "__main__":
    main()
