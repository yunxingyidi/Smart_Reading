class strBuffer:
    def __init__(self):
        self.area = []

    def add_string(self, str):
        for c in iter(str):
            self.area.append(c)

    def output_string(self):
        s = ""
        l = len(self.area)
        if l <= 0:
            return "0", False
        else:
            for index in range(l):
                s += self.area[index]
                del self.area[index];
            return s, True
