import serial

class Data:
    def __init__(self):
        self.ser = serial.Serial(port="/dev/ttyAMA1", baudrate=115200
        ,timeout=1E-7, parity=serial.PARITY_EVEN, stopbits=1
        ,bytesize=8)

    def sent_byte(self, ):