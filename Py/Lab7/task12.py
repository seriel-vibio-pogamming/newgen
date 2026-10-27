exm = "a for apple b for boy c for cat d for dog"
def count(text):
    counts ={}
    for wordcount in text.split():
        counts[wordcount] = counts.get(wordcount, 0) + 1
    return counts

result = count(exm)
for word, wc in result.items():
    print(word, wc)
for word, wc in sorted(result.items()):
    print(word, wc)

def reverse_lookup(d, v):
    newkeys = []
    for key in d:
        if d[key] == v:
            newkeys.append(key)
    return newkeys

def invert_dictionary(d):
    inverted = {}
    for key in d:
        val = d[key]
        if val not in inverted:
            inverted[val] = reverse_lookup(d, val)
    return inverted

reverse_lookup(result, 1)
newdict = invert_dictionary(result)
print(newdict)