import serial
import compile_part.mytext
import RPi.GPIO as GPIO
import time
import strBuffer

class Data:
    def __init__(self, numlist):
        # self.ser = serial.Serial(port="/dev/ttyAMA1", baudrate=115200
        # ,timeout=1E-7, parity=serial.PARITY_EVEN, stopbits=1
        # ,bytesize=8)
        self.numbuffer = []

    def sent_byte(self):
        GPIO.setmode(GPIO.BOARD)
        Pinlist = [7, 11, 13, 15, 12, 16]
        GPIO.setup(Pinlist, GPIO.OUT)

        GPIO.output(7, self.numbuffer[0])
        GPIO.output(11, self.numbuffer[1])
        GPIO.output(13, self.numbuffer[2])
        GPIO.output(15, self.numbuffer[3])
        GPIO.output(12, self.numbuffer[4])
        GPIO.output(16, self.numbuffer[5])
        time.sleep(3)

    def choose(self, numlist):
        for i in range(len(numlist)):
            if(self.numlist[i] == 1):
                self.numbuffer = [0, 0, 0, 0, 0, 1]
                self.sent_byte()
            elif(self.numlist[i] == 2):
                self.numbuffer = [0, 0, 0, 0, 1, 0]
                self.sent_byte()
            elif (self.numlist[i] == 3):
                self.numbuffer = [0, 0, 0, 1, 0, 0]
                self.sent_byte()
            elif (self.numlist[i] == 4):
                self.numbuffer = [0, 0, 0, 1, 0, 1]
                self.sent_byte()
            elif (self.numlist[i] == 5):
                self.numbuffer = [0, 0, 0, 1, 1, 0]
                self.sent_byte()
            elif (self.numlist[i] == 6):
                self.numbuffer = [0, 0, 0, 1, 1, 1]
                self.sent_byte()
            elif (self.numlist[i] == 7):
                self.numbuffer = [0, 0, 1, 0, 0, 0]
                self.sent_byte()
            elif (self.numlist[i] == 8):
                self.numbuffer = [0, 0, 1, 0, 0, 1]
                self.sent_byte()
            elif (self.numlist[i] == 9):
                self.numbuffer = [0, 0, 1, 0, 1, 0]
                self.sent_byte()
            elif (self.numlist[i] == 10):
                self.numbuffer = [0, 0, 1, 0, 1, 1]
                self.sent_byte()
            elif (self.numlist[i] == 11):
                self.numbuffer = [0, 0, 1, 1, 0, 0]
                self.sent_byte()
            elif (self.numlist[i] == 12):
                self.numbuffer = [0, 0, 1, 1, 0, 1]
                self.sent_byte()
            elif (self.numlist[i] == 13):
                self.numbuffer = [0, 0, 1, 1, 1, 0]
                self.sent_byte()
            elif (self.numlist[i] == 14):
                self.numbuffer = [0, 0, 1, 1, 1, 1]
                self.sent_byte()
            elif (self.numlist[i] == 15):
                self.numbuffer = [0, 1, 0, 0, 0, 0]
                self.sent_byte()
            elif (self.numlist[i] == 16):
                self.numbuffer = [0, 1, 0, 0, 0, 1]
                self.sent_byte()
            elif (self.numlist[i] == 17):
                self.numbuffer = [0, 1, 0, 0, 1, 0]
                self.sent_byte()
            elif (self.numlist[i] == 18):
                self.numbuffer = [0, 1, 0, 0, 1, 1]
                self.sent_byte()
            elif (self.numlist[i] == 19):
                self.numbuffer = [0, 1, 0, 1, 0, 0]
                self.sent_byte()
            elif (self.numlist[i] == 20):
                self.numbuffer = [0, 1, 0, 1, 0, 1]
                self.sent_byte()
            elif (self.numlist[i] == 21):
                self.numbuffer = [0, 1, 0, 1, 1, 0]
                self.sent_byte()
            elif (self.numlist[i] == 22):
                self.numbuffer = [0, 1, 0, 1, 1, 1]
                self.sent_byte()
            elif (self.numlist[i] == 23):
                self.numbuffer = [0, 1, 1, 0, 0, 0]
                self.sent_byte()
            elif (self.numlist[i] == 24):
                self.numbuffer = [0, 1, 1, 0, 0, 1]
                self.sent_byte()
            else:
                self.numbuffer = [0, 1, 1, 0, 1, 0]
                self.sent_byte()

