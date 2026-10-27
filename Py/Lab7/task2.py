mat1 = [[1,2,3,4],
        [5,6,7,8]]
mat2 = [[8,7,6,5],
        [4,3,2,1]]
for row in range(0,2):
    for col in range(0,4):
        print(mat1[row][col]+mat2[row][col], end=" ")
    print()