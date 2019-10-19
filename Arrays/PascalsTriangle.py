def pascalsTriangle(rows):
    if rows == 0:
        print("Atleast one row is needed")
    arr = [[1]]
    for i in range(rows - 1):
        prev = arr[-1]
        next = [1]
        for j in range(len(prev) -1):
            next.append(prev[j] + prev[j+1])
        next.append(1)
        arr.append(next)
        
    print(arr)
    
pascalsTriangle(4)

#Time complexity: O(n^2) to generate n rows
#Space complexity: O(n^2)
