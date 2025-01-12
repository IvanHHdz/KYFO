from commands import command

def main():
    while True:
        usr = input()
        command(usr)
        print()

if __name__ == "__main__":
    main()