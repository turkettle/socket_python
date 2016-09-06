#!/usr/bin/python           # This is client.py file

# import socket               # Import socket module
#
# s = socket.socket()         # Create a socket object
# host = socket.gethostname() # Get local machine name
# port = 12345                # Reserve a port for your service.
#
# s.connect((host, port))
# print s.recv(1024)
# s.close                     # Close the socket when done


# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# ###################
# #@Python - Client TCP
# #@Gaetan
# #@date 06092016
# ###################

import socket

def user_exit(msg):
    return msg == 'quit'

target_host = "127.0.0.1"
target_port = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host,target_port))

request = raw_input("\n\rWhat you want to say?\n\rSay [quit] to exit.\n\r\n\r")

if user_exit(request):
    print '\n\rBye bye!!\n\r'
    client.send('\n\rUser wants to exit.\n\r')
    client.close()
else :
    client.send(request)
    client.close()

client.send(request)
response = client.recv(4096)
print response
