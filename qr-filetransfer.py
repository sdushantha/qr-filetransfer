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
import pathlib

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


def random_port():
	port = random.random()
	return str(port)[5:9]


def start_server(fname):
    PORT = random_port()
    LOCAL_IP = get_local_ip()
    
    if fname.startswith("/"):
    	os.chdir("/")

    if os.path.isdir(fname):
        zip_name = pathlib.PurePosixPath(fname).name

        try:
            path_to_zip = make_archive(zip_name, "zip", fname)
            fname = path_to_zip.replace(os.getcwd(), "")

        except PermissionError:
            print("PermissionError: Try with sudo")
            sys.exit()  
        

    handler = http.server.SimpleHTTPRequestHandler

    try:
        httpd = socketserver.TCPServer(("", int(PORT)), handler)
        
    except PermissionError:
        # An error sometimes occurs randomly. 
        print("Error: Please try again")

    address = "http://" + str(LOCAL_IP) + ":" + str(PORT) + "/" + fname

    print("Scan the following QR to start downloading.\nMake sure that your smartphone is connected to the same WiFi network as this computer.")
    print_qr_code(address)
    httpd.serve_forever()


def print_qr_code(address):
    qr = qrcode.QRCode(1)
    qr.add_data(address)
    qr.make()
    qr.print_tty()


def main():
    parser = argparse.ArgumentParser(description = "Transfer files over wifi from your computer to your mobile device by scanning a QR code without leaving the terminal.")

    parser.add_argument("-f", "--file",
			required=True,
			help="File to be shared")

    args = parser.parse_args()


    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()


    start_server(fname=args.file)


if __name__=="__main__":
	main()
