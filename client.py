#!/usr/bin/env python3

import socket
import sys

'''
arguments include 
exp arg1, arg2
mod arg1, arg2
'''
def get_arguments():
   arguments = sys.argv[1:]
   # encoding; if there are extra arguments they will be dropped
   return ":".join(arguments)

def scan_arguments():
    arguments = sys.argv[1:]
    if len(arguments) != 3:
        raise Exception(f"Improper number of arguments.")
    if arguments[0] != "exp" and arguments[0] != "mod":
        raise Exception(f"Unsupported operation requested: {arguments[0]}.")
    check_is_int(arguments[1])
    check_is_int(arguments[2])

def check_is_int(arg):
    try:
        return int(arg)  
    except Exception:
        raise Exception(f"Invalid argument: '{arg}' cannot be converted to an integer.")


# ensure that arguments are appropriate
try: 
    scan_arguments()
except Exception as e:
    print(e, " Shutting down client.")
    exit()

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
MSG = get_arguments()

print("client starting - connecting to server at IP", HOST, "and port", PORT)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f"connection established, sending request '{MSG}'")
    s.sendall(bytes(MSG, 'utf-8'))
    print("message sent, waiting for reply")
    data = s.recv(1024)

print(f"Received response: '{data!r}' [{len(data)} bytes]")
print("client is done!")
