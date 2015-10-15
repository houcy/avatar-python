"""
TCP stream communicator class. Modified 21 September 2015
@author Matthew Ruffell <msr50@uclive.ac.nz>
"""

from avatar.communicators.communicator import Communicator
import logging
import socket

log = logging.getLogger(__name__)

class TCPCommunicator (Communicator):
    """ Implements a communicator interface with a tcp socket.
        Compatible with all TCP implementations
    """
    
    def __init__ (self, ipaddress, port):
        """ Initialisation function. Abstract"""
        self.socket = None
        self.ipaddress = ipaddress
        self.port = port
        
    def connect (self):
        """ Establish a connection with the target device """
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.ipaddress, self.port))
        
    def disconnect (self):
        """ Close a connection with the target device """
        self.socket.close()
    
    def send (self, data):
        """ Send data bytes to the target device """
        sent = self.socket.send(bytes(data, "utf-8"))
        if sent == 0:
            log.error("Socket failed to send data")
        self.device.flush()
        
    def recieve (self, count):
        """ Recieve count bytes from the target device """
        recieved =  self.socket.recv(count)
        if recieved == b'':
            log.error("Socket failed to recieve data")
        else:
            log.info("Socket recieved: " + recieved)
        return recieved
