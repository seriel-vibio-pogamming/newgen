dictD = {
    'a': "A",
    'b': "B",
    'c': "C"
}
print(len(dictD))
print("A" in dictD)
print("a" in dictD)
for keys in dictD.keys():
    print(keys)
for keys in dictD.keys():
    print(keys, dictD[keys])