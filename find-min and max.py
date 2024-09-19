

a = [10,60,3,45,5,50,40]
for i in a:
    for j in a:
        if(j<i):
            i=j
print("Minimum value:",i)


b=[15,50,3,10]
for i in b:
    for j in b:
        if(j>i):
            i=j          
print("Maximum value:",i)

