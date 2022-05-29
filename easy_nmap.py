import argparse
import imp
from colorama import Fore, Style
import commands
import six
from getpass import getuser

def menu():
    nmap = commands.Nmap()
    parse = argparse.ArgumentParser(description="Easy Nmap Menu.")
    parse.add_argument('--ip', dest='ip', help='Direccion IP. Ejemplo: 192.168.1.10')
    parse.add_argument('--ip-net', dest='ipnet', help='Subred y mascara. Ejemplo: 192.168.1.0/24')
    args = parse.parse_args()

    if args.ip != None:
        try:
            print("""
        ESCANEO
    [1.1] Escaneo TCP SYN.
    [1.2] Escaneo Sistema Operativo.
    [1.3] Escaneo Sistema Operativo y Servicios.
    [1.4] Escaneo Servicios Estandar.
    [1.5] Escaneo Agresivo de Servicios.\n
        SCRIPTS
    [2.1] Script de traceroute.
    [2.2] Extraer datos EXIF.
    [2.3] Script MySQL Enum.
    [2.4] Todos los scripts.
            """)
            op = input(Fore.GREEN + Style.BRIGHT +"""
    ┌──("""+getuser()+"""㉿hackerdivulgation)-[EasyNmap]
    └─$ """+ Fore.RESET + Style.RESET_ALL)
            if op == "1.1":
                nmap.set_ip_command(args.ip, "-sS")
                nmap.getCommand()
            elif op == "1.2":
                nmap.set_ip_command(args.ip, "-O")
                nmap.getCommand()
            elif op == "1.3":
                nmap.set_ip_command(args.ip, "-A")
                nmap.getCommand()
            elif op == "1.4":
                nmap.set_ip_command(args.ip, "-sV")
                nmap.getCommand()
            elif op == "1.5":
                nmap.set_ip_command(args.ip, "-sV --version-intensity 5")
                nmap.getCommand()
            elif op == "2.1":
                nmap.set_ip_command(args.ip, "--traceroute --script traceroute-geolocation.nse")
                nmap.getCommand()
            elif op == "2.2":
                nmap.set_ip_command(args.ip, "--script http-exif-spider")
                nmap.getCommand()
            elif op == "2.3":
                nmap.set_ip_command(args.ip, "--script mysql-enum")
                nmap.getCommand()
            elif op == "2.4":
                nmap.set_ip_command(args.ip, "--script all")
                nmap.getCommand()

        except KeyboardInterrupt:
            print(Fore.RED + Style.BRIGHT +"\nSaliendo del programa..."+ Fore.RESET + Style.RESET_ALL)
    
    elif args.ipnet != None:
        try:
            print("""
    1. Escanear una subred completa.
    2. Escanear una subred simple.
            """)
            op = input("Ingrese la opcion: ")

        except KeyboardInterrupt:
            print("\nSaliendo del programa...")

def banner():
    print(Fore.GREEN + Style.BRIGHT + """
########::::'###:::::'######::'##:::'##::::'##::: ##:'##::::'##::::'###::::'########::
##.....::::'## ##:::'##... ##:. ##:'##::::: ###:: ##: ###::'###:::'## ##::: ##.... ##:
##::::::::'##:. ##:: ##:::..:::. ####:::::: ####: ##: ####'####::'##:. ##:: ##:::: ##:
######:::'##:::. ##:. ######::::. ##::::::: ## ## ##: ## ### ##:'##:::. ##: ########::
##...:::: #########::..... ##:::: ##::::::: ##. ####: ##. #: ##: #########: ##.....:::
##::::::: ##.... ##:'##::: ##:::: ##::::::: ##:. ###: ##:.:: ##: ##.... ##: ##::::::::
########: ##:::: ##:. ######::::: ##::::::: ##::. ##: ##:::: ##: ##:::: ##: ##::::::::
........::..:::::..:::......::::::..::::::::..::::..::..:::::..::..:::::..::..:::::::::
""" + Fore.RESET + Fore.BLUE + """
V1.0 | 2022
Autor: Alex Terreros    
Web: http://hackerdivulgation.com""" + Fore.RESET + Style.RESET_ALL)

def main():
    if six.PY2:
        print("Python version 2. \nPor favor actualice a Python version 3!!!")
    elif six.PY3:
        banner()
        menu()

if __name__ == "__main__":
    main()