import socket
import termcolor

def scan(target, ports):
    for port in range(1, ports):
        scan_port(target, ports)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print('[+] Port Opened ' + str(port))
        sock.close()
    except:
        print('[-] Port Closed ' + str(port))

targets = int(input('[*] Enter target to scan (Split them by ,): '))
ports = input('[*] Enter how many ports you want to scan: ')
if ',' in targets:
    print('[*] Scanning multiple targets')
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '), ports)
else:
    scan(targets, ports)