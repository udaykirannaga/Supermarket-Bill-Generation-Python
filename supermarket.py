# Supermarket Bill Generation
from datetime import datetime

Customer_name=input("Please Enter Your Name :")

# List of Items
lists='''
rice    Rs 110/kg
sugar   Rs 50/kg
salt    Rs 25/kg
oil     Rs 60/Liter
panner  Rs 120/Kg
chicken Rs 200/Kg

'''
# print(lists)
price=0
pricelist=[]
totalprice=0
Finalprice=0
ilist=[]
qlist=[]
plist=[]

# Rates for the items
items={
    'rice':110,
    'sugar':50,
    'salt':25,
    'oil':60,
    'panner':120,
    'chicken':200
}

option=int(input("for list of itmes press 1 :"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("If you want to buy press 1 or 2 for Exit :"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your Item :")
        quantity=int(input("Enter your Quantity :"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("Sorry you Entered item is not Available")
    else:
        print("You Entered wrong number")
    inp=input("Can i bill the items yes or no :")
    if inp=="yes":
        pass
        if finalamount!=0:
            print(25*"=","Uday kiran",25,"=")
            print(26*" ","Nizamabad")
            print("Name:",Customer_name,30*" ","Date",datetime.now())
            print(75*"-")
            print("sno",8*" ","items",8*"","quantity",3*" ","price")

            for i in range(len(pricelist)):
                print(i,8*" ",8*" ",ilist[i],3*" ",qlist[i],plist[i])
            print(75*"-")
            print(50*" ","TotalAmount:","Rs",totalprice)
            print("GST Amount",50*" ","Rs",gst)
            print(75*"-")
            print(50*" ","FinalAmount:","Rs",finalamount)
            print(75*"-")
            print(50*"-","Thanks for visiting 🙏🙏🙏 Visit Again 😍")
            # print(75*"-")

# print(price)


