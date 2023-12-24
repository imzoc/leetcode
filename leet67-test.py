import leet67

s = leet67.Solution()

assert s.addBinary('11', '1') == '100'
assert s.addBinary('1010', '1011') == '10101'

assert s.addBinary('1111', '1') == '10000'

assert s.addBinary('0', '0') == '0'

assert s.addBinary('10000000', '11') == '10000011'
