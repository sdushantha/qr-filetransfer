#!/usr/bin/env python3

import qrcode
import http.server
import socketserver
import random
import os
import socket
import argparse
import sys
from shutil import make_archive


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
    
    if file.startswith("/"):
    	os.chdir("/")

    if os.path.isdir(file):
        zip_name = file.split("/")
        zip_name = zip_name[-2]

        try:
            path_to_zip = make_archive(zip_name, "zip", file)
            file = path_to_zip.replace(os.getcwd(), "")
        except PermissionError:
            print("PermissionError: Try with sudo")
            exit()  
        

    handler = http.server.SimpleHTTPRequestHandler

    try:
        httpd = socketserver.TCPServer(("", int(PORT)), handler)
    except:
        # An error sometimes occurs randomly. 
        print("Error: Please try again")

    address = "http://" + str(LOCAL_IP) + ":" + str(PORT) + "/" + file

    print("Scan the following QR to start downloading.\nMake sure that your smartphone is connected to the same WiFi network as this computer.")
    make_qr(address)
    httpd.serve_forever()


def make_qr(address):
    qr = qrcode.QRCode(1)
    qr.add_data(address)
    qr.make()
    qr.print_tty()


def main():
	parser = argparse.ArgumentParser(description = "Transfer files over wifi from your computer to your mobile device by scanning a QR code without leaving the terminal.")

	parser.add_argument("-f", "--file",
			type=str,
			required=True,
			help = "File to be shared")

	args = parser.parse_args()


	if len(sys.argv) == 1:
		parser.print_help()

	elif args.file:
		start_server(file=args.file)


if __name__=="__main__":
	main()
