Names = ["Priya","Naga","Mythily","Nisha","Devi"]
Amount = (1000,2000,3000,4000,5000)
amount = list(Amount)
sender = input("Enter the sender name:")
receiver = input("Enter the receiver name:")
send= int(input("Enter the amount:"))
j = 0
for i in Names:
    if (i == sender):
        print("Sender is available")
        available =  amount[j]
        print(sender,"Available amount :",amount[j])
        print(sender,"Balance amount:",amount[j]-send)
        amount[j] = amount[j]-send
    elif(i == receiver):
        print()
        print("Receiver name:",receiver)
        print(receiver,"Available amount:",amount[j])
        print(receiver,"total amount:",amount[j]+send)
        amount[j] = amount[j]+send
        Amo= tuple(amount)
        print(Amo)
        print(type(Amo))
j+=1


