#! /bin/python3
## Colors
# Author: Mrx04programmer
# Github : https://github.com/mrx04programmer
import socket, os
import sys
''' from scapy.all import sniff
from scapy.all import * '''
from datetime import datetime

sh = os.system
# Dataports ->
smbports = [139, 137, 138, 445, 631]
httpports = [80, 8080, 8090]
oports = [22, 2222, 2121, 1234, 4444, 21, 9999]
dataports = [3306, 8027, 8000, 88]
savesports = [443, 442]
def clear():
    sh("clear")

def main():
    def banner(ip):
        #clear()
        print(f"<h6 class='alert alert-dark'>[*] Escaneo iniciado en : {ip}</h6>")
        
    def start(ip):
        banner(ip)
        hostbyname = socket.gethostbyname(ip)
        try:
            for port in range(1, 65535):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                result = s.connect_ex((ip, port))
                if (result == 0):
                    print(f"<h6 class='alert alert-success'>[+] Se encontro el puerto {port} </h6>")
                    if (port in smbports):
                        print(f"<h6 class='alert alert-warning'>[+] SMB Ataque vulnerable !</h6>")
                    elif (port in httpports):
                        print(f"<h6 class='alert alert-warning'>[+] HTTP Ataque vulnerable !</h6>")
                    elif (port in oports):
                        print(f"<h6 class='alert alert-warning'>[+] PointerSever Ataque vulnerable !</h6>")
                    elif (port in dataports):
                        print(f"<h6 class='alert alert-warning'>[+] SQL-Injection Ataque vulnerable !</h6>")
                    elif (port in savesports):
                        print(f"<h6 class='alert alert-danger'>[o] Puerto muy seguro</h6>")
                    s.close()
            print(f"<h6 class='alert alert-dark'>{datetime.now()}  Escaneo terminado exitosamente </h6>")
        except KeyboardInterrupt:
            print(f"Bye bye.")
        except socket.gaierror:
            print(f"<h6 class='alert alert-danger'>El dispositivo {ip} no esta disponible o no tiene internet.</h6>")
            sys.exit()
        except socket.error:
            print(f"<h6 class='alert alert-danger'>Tu dispositivo local no responde !</h6>")
            sys.exit()


    def run():
        try:
            ip = sys.argv[1]
            start(ip)
        except IndexError:
            print(f"Falta establecer la ip.\nUtiliza: {sys.argv[0]} <ip>")
            exit()
    run()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"Error -> {e} en la linea ")