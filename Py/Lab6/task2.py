def printNumbers(n1,n2,n3):
    print(n1,n2,n3)

m1, m2, m3 = 10, 20, 30
printNumbers(m1,m2,m3)
printNumbers(n2=m2, n1=m3, n3=m1)

print("test", end=",")