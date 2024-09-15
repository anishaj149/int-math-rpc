#!/usr/bin/env python3

import socket

def scan_arguments(data):
    arguments = data.decode("utf-8").split(":")

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

def process_arguments(data):
    #bytes --> string
    args = data.decode("utf-8").split(":")
    return args[0], int(args[1]), int(args[2])

def identify_operation(operation):
    if operation == "mod": return "modulo"
    if operation == "exp": return "exponentiation"

def complete_operation(operation, arg1, arg2):
    if operation == "mod": 
        return arg1 % arg2
    if operation == "exp":
        return arg1 ** arg2

def get_final_message(operation, arg1, arg2, result):
    msg = ""
    if operation == "mod": 
        msg = f"{arg1} % {arg2} = {result}"
    if operation == "exp":
        msg =  f"{arg1} ** {arg2} = {result}" 

    # encode final msg
    return bytes(msg, 'utf-8')
   
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

print("server starting - listening for connections at IP", HOST, "and port", PORT)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected established with {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break

            print(f"Received client message: '{data!r}' [{len(data)} bytes]")

            #scan input
            try: 
                scan_arguments(data)
                good_input = True
            except Exception as e:
                print("Received malformed request from client. ", e)
                conn.sendall(bytes("Received malformed request. " + str(e), 'utf-8'))
                break

            #decode data
            operation, arg1, arg2 = process_arguments(data)
            print(f"Requested operation is '{identify_operation(operation)}' on arguments {arg1} and {arg2}") 

            #perform operation
            result = complete_operation(operation, arg1, arg2)
            print(f"Result of operation: {result}")

            #send message
            final_message = get_final_message(operation, arg1, arg2, result)
            print(f"sending result message'{final_message!r}' back to client")
            conn.sendall(final_message)

print("server is done!")
