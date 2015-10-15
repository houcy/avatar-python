"""
Serial device communicator class. Modified 22 August 2015
@author Matthew Ruffell <msr50@uclive.ac.nz>
"""

from avatar.communicators.communicator import Communicator
import logging
import serial

log = logging.getLogger(__name__)

class SerialCommunicator (Communicator):
    """ Implements a communicator interface with a serial port.
        Compatible with most serial and USB serial ports.
        Note that pySerial is a dependancy.
    """
    
    def __init__ (self, port, baudrate, bytesize, parity, stopbits):
        """ Initialisation function. Abstract"""
        self.device = None
        self.port = port
        self.baudrate = baudrate
        self.bytesize = bytesize
        self.parity = parity
        self.stopbits = stopbits
        
    def connect (self):
        """ Establish a connection with the target device """
        try:
            self.device = serial.Serial(self.port, self.baudrate, self.bytesize,
                          self.parity, self.stopbits)
        except ValueError as argument:
            log.error("Value out of range. Reason: ", argument)
        except SerialException as argument:
            log.error ("Failed to connect to communicator device. Reason: ", 
                       argument)
        
    def disconnect (self):
        """ Close a connection with the target device """
        self.device.close()
    
    def send (self, data):
        """ Send data bytes to the target device """
        self.device.write(bytes(data, "utf-8"))
        self.device.flush()
        
    def recieve (self, count):
        """ Recieve count bytes from the target device """
        recieved = self.device.read(count)
        if recieved == '':
            log.error("Failed to recieve data from UART")
        else:
            log.info("UART recieved: " + recieved)
        return recieved
