dictABC = {
    "a": "A",
    "b": "B",
    "c": "C",
    "d": "D"
}

def reverse_lookup(d, v):
    for key in d:
        if d[key] == v:
            print(key)

reverse_lookup(dictABC, "A")
reverse_lookup(dictABC, "B")
reverse_lookup(dictABC, "C")
reverse_lookup(dictABC, "D")