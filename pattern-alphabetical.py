# printing alphabets using chr

for i in range(65,71,1):
    j=65
    while(i>j):
        print(chr(j),end=" ")
        j+=1
    print("\n")
