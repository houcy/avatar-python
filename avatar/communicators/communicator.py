"""
Communicator class. Modified 22 August 2015.
@author Matthew Ruffell <msr50@uclive.ac.nz>
"""

class Communicator (object):
    """
        Generic abstract class for communicating with a target device.
        Examples could be serial, usb, etehernet or firewire.
    """
    
    def __init__ (self):
        """ Initialisation function. Abstract"""
        assert(False)
        
    def connect (self):
        """ Establish a connection with the target device """
        assert (False)
        
    def disconnect (self):
        """ Close a connection with the target device """
        assert (False)
    
    def send (self, data):
        """ Send data bytes to the target device """
        assert (False)
        
    def recieve (self, count):
        """ Recieve count bytes from the target device """
        assert (False)
