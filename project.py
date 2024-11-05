class products:
    def __init__(self):
        self.views = {
                1:{"Id":1,"Name":"Apple","Price":200,"Stock":50,"Expire date":"07.11.2024"},
                2:{"Id":2,"Name":"Mazza","Price":100,"Stock":30,"Expire date":"01.11.2024"},
                3:{"Id":3,"Name":"Dairy milk","Price":175,"Stock":50,"Expire date":"21.01.2025"},
                4:{"Id":4,"Name":"Rice","Price":70,"Stock":60,"Expire date":"27.10.2025"},
                5:{"Id":5,"Name":"Hair serum","Price":520,"Stock":40,"Expire date":"30.06.2025"},
                6:{"Id":6,"Name":"Wheatflour","Price":50,"Stock":20,"Expire date":"24.07.2025"},
                7:{"Id":7,"Name":"Biscuit","Price":50,"Stock":10,"Expire date":"30.01.2025"},
                8:{"Id":8,"Name":"Yippee","Price":60,"Stock":40,"Expire date":"26.10.2025"},
                9:{"Id":9,"Name":"Soap","Price":40,"Stock":50,"Expire date":"29.10.2025"},
                10:{"Id":10,"Name":"Butterscotch","Price":200,"Stock":90,"Expire date":"25.01.2025"}
                }
    def view(self):
        for i,j in self.views.items():
            print("\n")
            for k,l in j.items():
                print(k,":",l)

    # add new product

    def add(self):
        i = input("Enter the id:")
        add = ["Id","Name","Price","Stock","Expire date"]
        def get(value):
            y = input(f"Enter {value}:")
            if value == "Price":
                y = int(y)
            elif value == "Stock":
                y = int(y)
            return (value,y)
        print("\n")
        d = dict(map(get,add))
        print("\n","Recently added:",d,"\n")
        self.views[i]= d
        for a1,a2 in self.views.items():
            print("\n")
            for a3,a4 in a2.items():
                print(a3,":",a4)

    #Search the product
                
    def search(self):
        d = input("Enter the name to search the product:")
        def search1(v):
            i,j = v
            return j["Name"].lower() == d.lower()
        z = filter(search1,self.views.items())
        y = dict(z)
        for k,q in y.items():
            print("\n")
            for s,r in q.items():
                print(s,":",r)
                
    #Delete the expired product 
    def expiredate(self):
        da = input("Enter the expired date:")
        for r,j in self.views.items():
            if j["Expire date"] == da:
                del j["Id"]
                del j["Price"]
                del j["Stock"]
                del j["Expire date"]
                print("\n")
                print("Deleted successfully because the product has expired:")
                print("\n")
                for m,n in j.items():
                    print(m,":",n)
                

    

class customer1(products):
    
    def product1(self):
        totalcost = 0
        items = []   # selected products is store in this empty list
        
        while True:
            
            productname = input("Enter the product name: ")
            quantity = int(input("Enter the quantity: "))
            
            for product in self.views.values():
                if product["Name"].lower() == productname.lower():
                    if product["Stock"] >= quantity:      # Check stock is available or not
                        product["Stock"] -= quantity      
                        totalprice = product["Price"] * quantity
                        totalcost += totalprice
                        items.append({                      
                            "Product name":productname,
                            "Quantity":quantity,
                            "Total price":totalprice
                            })
                    else:
                        print("Out of stock")
                    break
            else:
                print("Product is not available")
                
            print("\n")
            add = input("Do you want to shop(yes/no):")
            
            print("\n")
            if add == "no":
                if items:
                    print("--Billing--","\n")
                    for item in items:
                        print("="*48)
                        print("Product:",item['Product name'],"\t", "Quantity:",item['Quantity'],"\t", "Item Cost:",item['Total price'],"\n")
                    print("Total price of all product is:","\t",totalcost,"\n")
                    print("..Thankyou for shopping..")
                    break
                    
pr = products()
pr1 = customer1()                   
print("--Welcome to all--")
while True:
    print("\n")
    print("--Enter your option--")
    print("1. View Products")
    print("2. Add Products")   
    print("3. Search the products")
    print("4. Expire date")
    print("5. Customer products Lists")
    print("6. Exit")
    a = int(input("Enter the chioce(1/2/3/4/5/6):"))
    if a == 1:
        print("\n","~~Products Lists~~")
        pr.view()
    elif a == 2:
        print("\n","~~Add new products~~","\n")
        pr.views = pr1.views
        pr.add()
    elif a == 3:
        print("\n","~~Search the product~~","\n")
        pr.search()
    elif a == 4:
        print("\n","~~Delete the expired products~~","\n")
        pr.expiredate()
    elif a == 5:
        print("\n","~~Customer Product Lists and billing~~","\n")
        pr1.views = pr.views
        pr1.product1()
    elif a == 6:
        print("\n","~~Thankyou for all~~","\n","---Come again---")
        break
    else:
        print("Invalid number")
        break

