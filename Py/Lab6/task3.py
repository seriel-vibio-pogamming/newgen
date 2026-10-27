def addInterest(bal, rate):
    newBalance = bal * (1 + rate)
    bal = newBalance
def test():
    amount = 1000
    rate = 0.05
    addInterest(amount, rate)
    print("My current balance is:", amount)
test()