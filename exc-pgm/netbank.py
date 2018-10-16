""" make the program that computes the net amount of a bank account based a transaction log from user input at the format of D 500 W 300"""

netAmount = 0
while True:
    s = input()
    if not s:
        break
#splitting the amount value using whitespace
    values = s.split(" ")
    operation = values[0]
    amount = int(values[1])
#the operation becomes deposit the netamount can be increase
    if operation=="D":
        netAmount+=amount
#the operation becomes withdrawal the netamount can be decrease
    elif operation=="W":
        netAmount-=amount
    else:
        pass
#print appropriate result
print(netAmount)
