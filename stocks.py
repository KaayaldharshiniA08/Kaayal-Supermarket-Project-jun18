Top=250
Jean=490
Sudi=450
Saree=500

def Girls_Season():
    try:
        print("----Top---->  250/-\n ---Jean---->  490/- \n----Sudi--->  450/-\n ----Saree---->  500/-")
        your_order=input("Enter Your product name:")
        if your_order=="Top":
            how_many=int(input(f"how many {your_order} you want:"))
            Total=Top*how_many
            Gst=16
            cgst=Top*((Gst/2)/100)
            Sgst=cgst
            affter_total=Total+Sgst+cgst
            if affter_total>=1100:
                discount=affter_total-100
                print(f"Awesome!! {affter_total} \n Your Purchasing Price Has Been More Than 1100 ,So Your Discount Amount is {discount}")
                f=open("bill.txt","w")
                f.write(f"your total bill amount is {affter_total} So, your discount amount is {discount}")
            else:
                print(f"Super!! Your Purchasing Price is {affter_total}")
                f=open("bill.txt","w")
                f.write(f"your total bill amount is {affter_total} ")
        elif your_order=="Jean":
             how_many=int(input(f"how many {your_order} you want:"))
             Total=Jean*how_many
             Gst=16
             cgst=Jean*((Gst/2)/100)
             Sgst=cgst
             affter_total=Total+Sgst+cgst
             if affter_total>=1200:
                discount=affter_total-100
                print(f"Awesome!! {affter_total} \n Your Purchasing Price Has Been More Than 1200 ,So Your Discount Amount is {discount}")
                f=open("bill.txt","w")
                f.write(f"your total bill amount is {affter_total} So, your discount amount is {discount}")
             else:
                print(f"Super!! Your Purchasing Price is {affter_total}")
                f=open("bill.txt","w")
                f.write(f"your total bill amount is {affter_total} ")
        elif your_order=="Sudi":
             how_many=int(input(f"how many {your_order} you want:"))
             Total=Sudi*how_many
             Gst=16
             cgst=Sudi*((Gst/2)/100)
             Sgst=cgst
             affter_total=Total+Sgst+cgst
             if affter_total>=1200:
                 discount=affter_total-100
                 print(f"Awesome!! {affter_total} \n Your Purchasing Price Has Been More Than 1200 ,So Your Discount Amount is {discount}")
                 f=open("bill.txt","w")
                 f.write(f"your total bill amount is {affter_total} So, your discount amount is {discount}")
             else:
                  print(f"Super!! Your Purchasing Price is {affter_total}")
                  f=open("bill.txt","w")
                  f.write(f"your total bill amount is {affter_total} ")
        elif your_order=="Saree":
            how_many=int(input(f"how many {your_order} you want:"))
            Total=Saree*how_many
            Gst=16
            cgst=Saree*((Gst/2)/100)
            Sgst=cgst
            affter_total=Total+Sgst+cgst
            if affter_total>=1500:
                discount=affter_total-100
                print(f"Awesome!! {affter_total} \n Your Purchasing Price Has Been More Than 1500 ,So Your Discount Amount is {discount}")
                f=open("bill.txt","w")
                f.write(f"your total bill amount is {affter_total} So, your discount amount is {discount}")
            else:
                print(f"Super!! Your Purchasing Price is {affter_total}")
                f=open("bill.txt","w")
                f.write(f"your total bill amount is {affter_total} ")
        else:
            print("pls give correct order name")

    except:
        print("Pls Enter the given products")

Shirt=450
Jeans=550
Pant=469

def Boys_Season():
    try:
        print("----Shirt---->  449/-\n ---Jean---->  559/- \n----Pant--->  469/-\n ")
        your_order=input("Enter Your product name:").lower()
        if your_order == "shirt":
            how_many = int(input(f"How many {your_order}s do you want: "))
            Total = 449 * how_many
            Gst = 16
            cgst = 449* ((Gst / 2) / 100)
            Sgst = cgst
            after_total = Total + Sgst + cgst
            if after_total >= 1100:
                discount = after_total - 100
                print(f"Awesome!! {after_total} \n Your Purchasing Price Has Been More Than 1100 ,So Your Discount Amount is {discount}")
                f=open("bill.txt","w")
                f.write(f"your total bill amount is {after_total} So, your discount amount is {discount}")
            else:
                print(f"Super!! Your Purchasing Price is {after_total}")
                f=open("bill.txt","w")
                f.write(f"your total bill amount is {after_total} ")
        elif your_order == "jeans":
             how_many = int(input(f"How many {your_order}s do you want: "))
             Total = 559 * how_many
             Gst = 16
             cgst = 559 * ((Gst / 2) / 100)
             Sgst = cgst
             after_total = Total + Sgst + cgst
            
             if after_total >= 1200:
                discount = after_total - 100
                print(f"Awesome!! {after_total} \n Your Purchasing Price Has Been More Than 1200 ,So Your Discount Amount is {discount}")
                f=open("bill.txt","w")
                f.write(f"your total bill amount is {after_total} So, your discount amount is {discount}")
             else:
                print(f"Super!! Your Purchasing Price is {after_total}")
                f=open("bill.txt","w")
                f.write(f"your total bill amount is {after_total} ")
        
        elif your_order == "pant":
             how_many = int(input(f"How many {your_order}s do you want: "))
             Total = 469 * how_many
             Gst = 16
             cgst = 469 * ((Gst / 2) / 100)
             Sgst = cgst
             after_total = Total + Sgst + cgst
            
             if after_total >= 1200:
                 discount = after_total - 100
                 print(f"Awesome!! {after_total} \n Your Purchasing Price Has Been More Than 1200 ,So Your Discount Amount is {discount}")
                 f=open("bill.txt","w")
                 f.write(f"your total bill amount is {after_total} So, your discount amount is {discount}")
             else:
                  print(f"Super!! Your Purchasing Price is {after_total}")
                  f=open("bill.txt","w")
                  f.write(f"your total bill amount is {after_total} ")
                  f=open("bill.txt","w")
                  f.write(f"your total bill amount is {after_total} ")
        else:
            print("pls give correct order name")
    except:
        print("Pls Enter the given products")
    