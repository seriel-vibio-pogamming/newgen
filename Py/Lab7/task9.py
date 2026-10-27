dictE = {
    'a': "A",
    'b': "B",
    'c': "C"
}
newDict = dict()
callDict = dict(dictE)

print(newDict)
print(callDict)
newDict["a"] = "abc"
print(newDict)
del newDict["a"]
print(newDict)