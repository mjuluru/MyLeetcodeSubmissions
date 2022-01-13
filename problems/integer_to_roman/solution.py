class Solution:
    def intToRoman(self, num: int) -> str:
        result = ''
        i = num
        k = 1
        a1 = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        a2 = ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        a3 = ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        a4 = ['M', 'MM', 'MMM']
        while i > 0:
            rem = i % 10
            while rem == 0:
                i = i//10
                k = k + 1
                rem = int(i % 10)
            if k == 1:
                result = a1[rem-1] + result
            elif k == 2:
                result = a2[rem-1] + result
            elif k == 3:
                result = a3[rem-1] + result
            elif k == 4:
                result = a4[rem-1] + result
            i = i//10
            k = k + 1
        return result