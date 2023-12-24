class Solution:
    def addBinary(self, a, b):
        s = ''
        i, carry = 0, 0
        ai, bi = int(a[-1]), int(b[-1])
        while i < min(len(a), len(b)) or ai + bi + carry > 1:
            ai = int(a[-1 - i]) if i < len(a) else 0
            bi = int(b[-1 - i]) if i < len(b) else 0
            s = str((carry + ai + bi) % 2) + s
            carry = carry + ai + bi >= 2
            i += 1
        if i < len(a):
            s = a[0:len(a) - i] + s
        if i < len(b):
            s = b[0:len(b) - i] + s
        return s
