iq = int(input("Please enter your IQ (rounded to nearest integer): "))

if iq >=130:
    print("Very Superior IQ")
elif iq >=120:
    print("Superior IQ")
elif iq >=110:
    print("High Average IQ")
elif iq>=90:
    print("Average IQ")
elif iq>=80:
    print("Low Average IQ")
elif iq>=70:
    print("Borderline IQ")
else:
    print("Extremely Low IQ")

# code with throw new error:
# iqinput = input("Please enter your IQ (rounded to nearest integer): ")
# while True:
#     try:
#         iq = int(iqinput)
#         if iq >= 130:
#             print("Very Superior IQ")
#         elif iq >= 120:
#             print("Superior IQ")
#         elif iq >= 110:
#             print("High Average IQ")
#         elif iq >= 90:
#             print("Average IQ")
#         elif iq >= 80:
#             print("Low Average IQ")
#         elif iq >= 70:
#             print("Borderline IQ")
#         else:
#             print("Extremely Low IQ")
#         break
#     except ValueError:
#         print("Please enter an integer!\n")
#         break


