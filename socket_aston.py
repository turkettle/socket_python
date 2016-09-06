#!/usr/bin/python           # This is server.py file

# import socket               # Import socket module
#
# s = socket.socket()         # Create a socket object
# host = socket.gethostname() # Get local machine name
# port = 12345                # Reserve a port for your service.
# s.bind((host, port))        # Bind to the port
# s.send('Whamy')
#
# s.listen(5)                 # Now wait for client connection.
# while True:
#    c, addr = s.accept()     # Establish connection with client.
#    print c
#    print addr
#    print 'Got connection from', addr
#    c.send('Thank you for connecting')
#    c.close()                # Close the connection


# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# ###################
# #@Python - Calculatrice
# #@Gaetan
# #@date 05092016
# ###################
#
import socket
import threading

##      FONCTIONS       ##

def handle_client(client_socket):
    request = client_socket.recv(2048)
    print "[*] Received: %s" % request
    response = raw_input("what you want to say ?\n")
    client_socket.send(response)
    client_socket.close()

##      SCRIPT         ##

bind_ip = "127.0.0.1"
bind_port = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip,bind_port))
server.listen(5)
print "[*] listening on %s:%d" %(bind_ip,bind_port)

client,addr = server.accept()
print "[*] Accepted connection from %s:%d" % (addr[0],addr[1])
# client_handler = threading.Thread(handle_client(client))
client_handler = threading.Thread(target = handle_client,args = (client,))
client_handler.start()
