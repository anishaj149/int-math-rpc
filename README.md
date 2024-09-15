# Extra Int Math

## Overview of Application 
The goal of the application is to request an operation on the client side, then perform the operation on the server side. The operations include modulo and exponentiation. The client receives the request as follows: "operation arg1 arg2".

The operation keywords possible are:
- mod 
- exp

example requests: 
- "mod 10 6" - results in server message "10 % 6 = 4"
- "exp 5 3" - results in server message "5 ** 3 = 125"

Malformed requests will have operations that are not part of the possible operation keywords list. Alternatively, they will have arguments that are non-integers. Lastly, only two arguments are expected. Requests will be scanned on both client and server side. 

example of malformed requests: 
- "modd 1 2" - this request has an incorrect operation 
- "exp 2.2 2" - this request has an non-integer argument
- "mod 1 2 3 4" - this request has too many arguments
- "exp 1" - this request has too few arguments

## Client->Server Message Format 
The client will send the server a message that encodes the information in the operation request. Each argument/operation is separated by the delimeter ":". The message to the server from the client will follow the general format "operation:arg1:arg2."

example messages: 
- "mod:10:6" - results from request "mod 10 6"
- "exp:5:3" - results from request "exp 5 3"

## Server->Client Message Format 
Upon completion of the operation, the server will send the client a message informing them of the operation's result. The message to the server from the client will follow the general format "arg1 operation_symbol arg2 = result"

Note that there exists a mapping f between the operation keywords and operation symbols. Namely, f("mod")="%" and f("exp")="**".

example messages: 
- "10 % 6 = 4" - results from client message "mod:10:6"
- "5 ** 3 = 125" - results from client message "exp:5:3"

## Example Output 

The following example will show a successful operation request. 

#### client trace 
client starting - connecting to server at IP 127.0.0.1 and port 65432

connection established, sending request 'mod:10:6'

message sent, waiting for reply

Received response: 'b'10 % 6 = 4'' [10 bytes]

client is done!

#### server trace
server starting - listening for connections at IP 127.0.0.1 and port 65432

Connected established with ('127.0.0.1', 65167)

Received client message: 'b'mod:10:6'' [8 bytes]

Requested operation is 'modulo' on arguments 10 and 6

Result of operation: 4

sending result message'b'10 % 6 = 4'' back to client

server is done!

## Acknowledgments
No outside help was used in this project. 