import mytext

str = " fergqervb "
a = mytext.alphabet2byte(str, len(str))
b = []
b = list(a)
c = []
for i in b:
    t = ord(i)
    if t >= 66:
        t -= 66
    c.append(t)
print(c)