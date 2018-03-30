import qrcode
import http.server
import socketserver
import random
from os import system, chdir
import socket
import argparse
import sys


white_block = '\033[0;37;47m  '
black_block = '\033[0;37;40m  '
new_line = '\033[0m\n'


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


def random_port():
	port = random.random()
	return str(port)[5:9]


def start_server(file):
    PORT = random_port()
    LOCAL_IP = get_local_ip()
    
    if "/" in file:
    	chdir("/")

    handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", int(PORT)), handler)
    address = "http://"+str(LOCAL_IP)+":"+str(PORT)+"/"+file

    print("Scan the following QR to start downloading.\nMake sure that your smartphone is connected to the same WiFi network as this computer.")
    make_qr(address)
    ser = httpd.serve_forever()


# It works yay :)
def make_qr(address):
    qr = qrcode.QRCode(1)
    qr.add_data(address)
    qr.make()
    output = white_block*(qr.modules_count+2) + new_line
    for mn in qr.modules:
        output += white_block
        for m in mn:
            if m:
                output += black_block
            else:
                output += white_block
        output += white_block + new_line
    output += white_block*(qr.modules_count+2) + new_line
    print(output)

#file = input("FILE: ")
#start_server(file=file)

def main():
	parser = argparse.ArgumentParser(description = "Transfer files over wifi from your computer to your mobile device by scanning a QR code without leaving the terminal.")

	parser.add_argument("-f", "--file",
			type=str,
			required=True,
			help = "File to be shared")

	args = parser.parse_args()


	if len(sys.argv) == 1: # if argument is given then show help
		parser.print_help()

	elif args.file:
		start_server(file=args.file)


if __name__=="__main__":
	main()
