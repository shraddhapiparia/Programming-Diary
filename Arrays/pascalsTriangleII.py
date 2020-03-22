class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        out = [1]
        if rowIndex == 0:
            return out
        for i in range(rowIndex):
            row = [1]
            for j in range(len(out)-1):
                row.append(out[j] + out[j+1])
            row.append(1)
            out = row
        return out
