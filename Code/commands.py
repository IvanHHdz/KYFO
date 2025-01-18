import os
from format import p_error, p_elemets, p_color
import re
from functools import partial
from shlex import split
from shutil import move

tree = {}
sf = None
auto = False

rute_slash = '/' if os.name == 'posix' else '\\'

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
            if os.name == 'nt':
                r = re.sub(r"^\./", gr().replace('\\', '\\\\') + '\\\\', rute)
                return r
            else:
                return re.sub(r"^\.", f"{gr()}", rute)
        elif re.match(r"^[\w/ \.-]*/.*", rute) or re.match(r"^[\w\\ \.-:]*\\.*", rute):
            return rute
        elif re.match(r"^0x[\da-f]+$", rute.lower()) and tree != {}:
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
            d += dirs(rute+rute_slash+ele[0][i])
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
                t[hex(id)] = rute+rute_slash+ele[0][i]
                id += print_id(ele[0][i], id, tab)
                sdt(rute+rute_slash+ele[0][i], tab+1, True, t, id)
                id += dirs(rute+rute_slash+ele[0][i])
            else:
                p_color(['|\t'*(tab-1)+'|-> ',ele[0][i]],['Yellow','Cyan'])
                sdt(rute+rute_slash+ele[0][i], tab+1)
    return t

# * Show Rute
def srt():
    p_color(ver_arg_rut(None), "White")

# * Assing a tree
def aat(arg1=None):
    rute = ver_arg_rut(arg1)
    if rute:
        global tree
        tree = sdt(arg1=rute, assing=True)

def mov(arg1, arg2):
    if arg1 == "#s" and sf:
        ori = sf
    else:
        ori = ver_arg_rut(arg1)
    des = ver_arg_rut(arg2) + rute_slash
    if ori and des:
        move(ori, des)
        p_color([f"'{ori}'", " was moved to ", f"'{des}'"],["Magenta","White", "Cyan"])
        if auto:
            sel('.')

def sel(arg1=None, arg2=None):
    if arg1:
        rute = ver_arg_rut(arg2)
        if not rute:
            return
        ele = ge(rute)
        for i in range(len(ele[0])):
            if not ele[1][i]:
                if ele[0][i] == arg1 or arg1 == '.':
                    p_color([f"'{ele[0][i]}'",", from ",f"'{rute}/'",", is now the selected file"],["Magenta", "White", "Cyan", "White"])
                    global sf
                    sf = rute + rute_slash + ele[0][i]
                    return
        p_error("Not files founded.")
    else:
        if sf:
            p_color([f"'{sf}'", ", from, is the selected file"],["Magenta", "White"])
        else:
            p_color("You haven't selected a file yet.","White")

def aut():
    global auto
    if auto:
        auto = False
        p_color("The automatic selection of files is off.", "Green")
    else:
        auto = True
        p_color("The automatic selection of files is on.", "Green")
        if not sf:
            sel('.')

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
            p(["\tmove <file> <rute>" , " - Moves a file to a new rute."])
            p(["\tsel <file>" , " - Select a file."])
            p(["\taut" , " - Activate/Desactivate the auto selection of files."])
#TODO agregar la documentacion
#TODO agregar las consideraciones para la correcta sintaxis de cada comando, en especial mov

# * Commands
def command(usr):
    command = split(usr)
    commands = {
        "srt" : srt,
        "lse" : lse,
        "doc" : doc,
        "sdt" : sdt,
        "aat" : aat,
        "mov" : mov,
        "sel" : sel,
        "aut" : aut
    }
    try:
        if len(command) == 1:
            return commands[command[0]]()
        elif len(command) == 2:
            return commands[command[0]](arg1 = command[1])
        else:
            return commands[command[0]](arg1 = command[1], arg2 = command[2])
    except:
        p_error("Sintax Error")
        doc(st = True)

def main():
    command('aat ./Example')
    command('aut')
    command('mov #s 0x3')

if __name__ == "__main__":
    main()
