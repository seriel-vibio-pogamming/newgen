name = input("Enter your full name: ")
fname, lname = name.split()
email = fname[0] + lname[:5] + "@connect.polyu.hk"
print("Your email is: " + email.lower())

myname = ["Quang", "Pham"]
n = " ".join(myname)
print(n)