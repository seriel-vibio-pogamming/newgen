nicknames =  {"Mickey":"Mickey mouse in Disney", "Minnie": "Minnie mouse in Disney"}
students = {"12345678d": ["name1", 10, 8],
            "12345679d": ["name2", 8, 9],
            "12345671d": ["name3", 7, 5]}
print(nicknames["Mickey"])
print(nicknames["Minnie"])
# print(students["12345678d"])
students["87654321d"] = ["name4", 10, 10]
for st in students:
    print(st)
    print(students[st])