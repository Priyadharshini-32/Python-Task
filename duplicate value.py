
#duplicate value

list = [10,20,20,30,70,70,40,50]
list1 = []
for i in list:
    if(i not in  list1):
        list1.append(i)
list=list1
print(list)



