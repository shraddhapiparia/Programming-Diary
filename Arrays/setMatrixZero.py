def setMatrixZero(matrix):
    row = set()
    col = set()
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if matrix[i][j] == 0:
                row.add(i)
                col.add(j)
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if i in row or j in col:
                matrix[i][j] = 0
    print(matrix)
                
setMatrixZero([[1,3,3],[1,1,1],[3,0,4],[3,3,3]])

#Time : O(2*m*n) space: O(m+n) for sets
