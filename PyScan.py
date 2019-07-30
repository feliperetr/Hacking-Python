import socket

def scan():
    ports = [80, 443, 8080, 518]
    ip = raw_input('\033[1;31m[*] - IP Scan:')
    for x in ports:
        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scanner.settimeout(1)
        alvo = scanner.connect_ex(ip, ports)
        if alvo == 0:
            print('\033[1;31m[+] - Port', x ,'\033[1;32mOPEN')
scan()
