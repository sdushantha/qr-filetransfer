#!/usr/bin/env python3

import qrcode
import http.server
import socketserver
import random
import os
import socket
import argparse
import sys
from shutil import make_archive, move, rmtree, copy2
import pathlib
import signal

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


def random_port():
    return random.randint(1024, 65535)


def start_server(fname):
    PORT = random_port()
    LOCAL_IP = get_local_ip()
    # Using .tmpqr since .tmp is very common
    TEMP_DIR_NAME = ".tmp_qr"

    # Variable to mark zip for deletion, if the user uses a folder as an argument
    delete_zip = 0

    # Checking if given fname is a path
    if fname.startswith("/"):
        os.chdir("/")
    # Checking if given file name or path is a directory
    if os.path.isdir(fname):
        zip_name = pathlib.PurePosixPath(fname).name

        try:
            # Zips the directory
            path_to_zip = make_archive(zip_name, "zip", fname)
            fname = path_to_zip.replace(os.getcwd(), "")
            # The above line replacement leaves a / infront of the file name
            fname = fname.replace("/", "")
            delete_zip = fname
        except PermissionError:
            print("PermissionError: Try with sudo")
            sys.exit()

    # Makes a directory name .tmpqr and stores the file there
    os.makedirs(TEMP_DIR_NAME)
    
    try:
        # Move the file to .tmpqr
        copy2(fname, TEMP_DIR_NAME)
    except FileNotFoundError:
        print("File not found!")
        rmtree(TEMP_DIR_NAME)
        sys.exit()

    # Change our directory to .tmpqr
    os.chdir(TEMP_DIR_NAME)

    handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", PORT), handler)

    # This is the url to be encoded into the QR code
    address = "http://" + str(LOCAL_IP) + ":" + str(PORT) + "/" + fname

    print("Scan the following QR to start downloading.\nMake sure that your smartphone is connected to the same WiFi network as this computer.")
    print_qr_code(address)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        os.chdir("..")
        rmtree(TEMP_DIR_NAME)
    # If the user sent a directory, a zip was created and then copied to the temporary directory, this deletes the first created zip
    if delete_zip != 0:
        os.remove(delete_zip)
    print("\nExiting...")
    sys.exit()

def print_qr_code(address):
    qr = qrcode.QRCode(1)
    qr.add_data(address)
    qr.make()
    qr.print_tty()


def main():
    # This disables CTRL+Z while the script is running
    signal.signal(signal.SIGTSTP, signal.SIG_IGN)
    parser = argparse.ArgumentParser(description = "Transfer files over WiFi from your computer to your mobile device by scanning a QR code without leaving the terminal.")

    parser.add_argument("-f", "--file",
			required=True,
			help="File to be shared")

    args = parser.parse_args()

    # If no argument is given or invalid agrument then it shows help
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()


    start_server(fname=args.file)


if __name__=="__main__":
	main()
