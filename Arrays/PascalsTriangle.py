class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        out = [[1]]
        if numRows == 0:
            return None
        for i in range(numRows-1):
            row = [1]
            prev = out[-1]
            for j in range(len(prev)-1):
                row.append(prev[j] + prev[j+1])
            row.append(1)
            out.append(row)
        
    print(out)
    
pascalsTriangle(4)

#Time complexity: O(n^2) to generate n rows
#Space complexity: O(n^2)
