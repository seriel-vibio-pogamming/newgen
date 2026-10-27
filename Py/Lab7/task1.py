# mat = [ 1, 2, "3", [4, [5,7,8], 6] ]
# print(mat)
# print(type(mat))
# print(mat[3][1][0])
# print(len(mat))
#
mat = [[1,2],
       [3,4]]

print(mat[0][0])
print(mat[0][1])
print(mat[1][0])
print(mat[1][1])
for row in range(0,2):
    for col in range(0,2):
        print(mat[row][col], end="")
    print("")
