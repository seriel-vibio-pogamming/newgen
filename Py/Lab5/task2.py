str1 = "sausage"
str2 = "eggs"
print(str1 + "and" + str2)
print(len(str1 + "and" + str2))
print(3 * str1)
print(3 * str1 + "and" + 2 * str2)
print(len(3 * str1 + "and" + 2 * str2))

for ch in str1:
    print(ch, end=",")