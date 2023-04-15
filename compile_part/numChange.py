import mytext
import cv_part.strBuffer as bu

class numChange:
    def __init__(self):
        self.buffer = bu.strBuffer()

    def add(self, buffer):
        self.buffer = buffer

    def a2num(self, len):
        str = self.buffer.output_string()
        numstr = mytext.alphabet2byte(str, len(str))
        numlist = []
        numlist = list(numstr)
        res = []
        for i in numlist:
            num = ord(i)
            if num >= 66:
                num -= 66
            res.append(num)
        return res

