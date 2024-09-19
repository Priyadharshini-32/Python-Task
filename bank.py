

Names = "Priya","Naga","Mythily","Nisha","Revathi"
money = 1000,2000,3000,4000,5000
a = input("Enter the sender name:")
b = input("Enter the receiver name:")
c = int(input("Enter the amount:"))
for i in Names:
    if(i==a):
        print("Sender name is available")
        g = Names.index(i)
        print(a,"available amount:",money[g])
        print(a,"Balance amount:",money[g]-c)
        break
for j in Names:
    if(j==b):
        
        print("Receiver:",b)
        f = Names.index(j)
        print("Receiver Balance:",money[f])
        print("Total amount for receiver:",money[f]+c)
        break
else:
    print("not Avaliable")
