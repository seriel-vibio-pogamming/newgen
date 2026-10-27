Group1 = {
    "01010101d": "Brian",
    "02020202d": "Jimmy",
    "03030303d": "David"
}
Group2 = {
    "04040404d": "John",
    "05050505d": "Lisa"
}
Group3 = {
    "06060606d": "Angela",
    "07070707d": "Alice",
    "08080808d": "Bob",
    "09090909d": "Charlie"
}

groups = [
    ("Group1", Group1),
    ("Group2", Group2),
    ("Group3", Group3)
]

for groupname, id in groups:
    for sid, name in id.items():
        print(sid, name, end="")
        print(" in " + groupname)

idfind = input("Enter the ID of the student you wish to find: ")

for groupname, id in groups:
    if idfind in id:
        print(id[idfind], end="")
        print(" in " + groupname)
        exit()
print("The student ID you entered does not exist")
