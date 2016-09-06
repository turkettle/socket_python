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

target_host = "127.0.0.1"
target_port = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host,target_port))

request = raw_input("what you want to say?\n")
client.send(request)
response = client.recv(4096)
print response
