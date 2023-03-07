import threading
import globalvar as gl

class Sound(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.read_text = 0
        self.pos = 0
        self.state = True

    def change_state(self, state):
        self.state = state
        return not self.state

    def read(self, text):
        self.read_text = text

    def run(self):
        self.pos = 0
        while self.pos < len(self.read_text):
            if self.state:
                ############
                #此处输出音频#
                ############
                self.pos += 1
            else:
                pass
