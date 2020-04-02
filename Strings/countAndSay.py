class Solution:
    def countAndSay(self, n: int) -> str:
        base = 1
        for i in range(n-1):
            count = 0
            prev = 11
            dicti = {}
            while base != 0:
                dig = base%10
                if dig == prev:
                    (val,ct) = dicti[count-1]
                    dicti[count-1] = (val,ct+1)
                else:
                    dicti[count] = (dig,1)
                    count += 1
                base //= 10
                prev = dig
            rev = ''
            for item in reversed(dicti):
                (term, freq) = dicti[item]
                rev += str(freq) + str(term)
            base = int(rev)
        return str(base)
