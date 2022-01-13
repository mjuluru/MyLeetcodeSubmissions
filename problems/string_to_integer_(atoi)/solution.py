
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip(" ")
        if s == '':
            return 0
        pos = True
        result = ''
        if s[0] == '-':
            pos = False
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        for i in range(0, len(s)):
            if s[i] in '0123456789':
                result = result + s[i]
            else:
                break
        if result != '':
            MAX = pow(2,31)-1
            MIN = 0- MAX - 1
            num = int(result)
            if MIN <= num and num <= MAX:
                if pos == True:
                    return num
                num = 0-num
                return num
            elif pos == False:
                return MIN
            elif pos == True:
                return MAX
        return 0
            