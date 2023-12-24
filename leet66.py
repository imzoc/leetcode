class Solution:
    def plusOne(self, digits):
        u = len(digits) - 1
        carry = 1
        while carry and u >= 0:
            if digits[u] == 9:
                digits[u] = 0
                u -= 1
                
            else:
                digits[u] += 1
                carry = 0
        if carry:
            digits.insert(0, 1)

        return digits
