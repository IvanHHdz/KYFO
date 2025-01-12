import os
from format import p_error, p_elemets, p_color
import re
from functools import partial
from shlex import split

tree = {}

# * Get Elements
def ge(rute):
    try:
        e = [[],[]]
        for item in os.listdir(rute):
            c_rute = os.path.join(rute, item)
            if os.path.isdir(c_rute):
                e[1].append(True)
            else:
                e[1].append(False)
            e[0].append(item)
        return e
    except:
        p_error("Invalid rute")
        return e

# * Verication of Arguments - Rute
def ver_arg_rut(rute):
    if rute:
        if re.match(r"^\./.+", rute):
            return re.sub(r"^\.", f"{gr()}", rute)
        elif re.match(r"^[\w/ \.-]*/.+", rute):
            return rute
        elif re.match(r"^0x[\da-f]+$", rute.lower()):
            p_color(tree[rute.lower()], 'Yellow')
            return tree[rute.lower()]
        else:
            p_error('Invalid Rute')
            return False
    return gr() if tree == {} else tree["0x0"]
    

# * List Elements
def lse(arg1 = None):
    rute = ver_arg_rut(arg1)
    if not rute:
        return
    p_elemets(ge(rute), "Cyan", "Magenta")

# * Get Rute 
def gr():
    return os.getcwd()

 # * Count the directories
def dirs(arg1):
    rute = ver_arg_rut(arg1)
    d = 0
    ele = ge(rute)
    for i in range(len(ele[0])):
        if ele[1][i]:
            d += 1
            d += dirs(rute+"/"+ele[0][i])
    return d

def print_id(dir, id, tab, i = 1):
    p_color(['|\t'*(tab-1)+'|-> '*i,dir, '\tid = ' + str(hex(id))],['Yellow','Cyan', 'White'])
    return 1


# * Show Tree
def sdt(arg1=None, tab=1, assing=False, t = {}, id = 0):
    rute = ver_arg_rut(arg1)
    if not rute:
        return
    ele = ge(rute)
    if tab == 1:
        if assing:
            t[hex(id)] = rute
            id += print_id(rute, id, tab, 0)
        else:
            p_color(rute, "Cyan")
    for i in range(len(ele[0])):
        if ele[1][i]:
            if assing:
                t[hex(id)] = rute+'/'+ele[0][i]
                id += print_id(ele[0][i], id, tab)
                sdt(rute+"/"+ele[0][i], tab+1, True, t, id)
                id += dirs(rute+"/"+ele[0][i])
            else:
                p_color(['|\t'*(tab-1)+'|-> ',ele[0][i]],['Yellow','Cyan'])
                sdt(rute+"/"+ele[0][i], tab+1)
    return t

# * Show Rute
def srt():
    p_color(gr(), "White")

# * Assing a tree
def aat(arg1=gr()):
    rute = ver_arg_rut(arg1)
    if rute:
        global tree
        tree = sdt(arg1=rute, assing=True)

# * Documentation
def doc(arg1=None,st = False):
    if st:
        p_error("Try 'doc' to see the documentation.")
    else:
        if arg1:
            pass
        else:
            print("Valid commands:")
            p = partial(p_color, c=["Green","White"])
            p(["\tsrt" , " - Show actual rute."])
            p(["\tlse <rute>"," - List the elements of a rute, the actual rute by default."])
            p(["\tdoc"," - Show the documentation."])
            p(["\tsdt <rute>", " - Show a tree of directories from a rute, the actual rute by default."])
            p(["\taat <rute>", " - Create a tree of directories with unique id from a rute, actual rute by the default."])
    #TODO agregar la documentacion

# * Commands
def command(usr):
    command = split(usr)
    commands = {
        "srt" : srt,
        "lse" : lse,
        "doc" : doc,
        "sdt" : sdt,
        "aat" : aat,
    }
    try:
        if len(command) == 1:
            return commands[command[0]]()
        else:
            return commands[command[0]](arg1 = command[1])
    except:
        p_error("Sintax Error")
        doc(st = True)

def main():
    aat()

if __name__ == "__main__":
    main()
