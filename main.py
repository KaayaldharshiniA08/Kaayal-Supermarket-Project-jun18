import datetime
import stocks
import smtplib

def current_date():
    x=datetime.datetime.now()
    print(x)


def send_order_confirmation(name, E):
    try:
        new_name=name
        receiver_email = "dharshinikaya37@gmail.com"
        for i in receiver_email:
            server=smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login("kayaldharshini5@gmail.com")
            message=(f"Dear {name}Order Confirmation from Dhara SuperMarket\n\nThank you for shopping with Dhara SuperMarket.\n\nYour order details are attached.\n\nBest Regards,\nDhara SuperMarket Team")
            message=("bill.txt")
            server.sendmail("kayaldharshini5@gmail.com","dharshinikaya37@gmail.com",message )
            print(f"Mail sent successfully to {receiver_email}")
 
    except:
        print("Pls enter your correct mail id")


def main():
    print("Welcome To Dhara SuperMarket")
    print("****Girls Season****\n----Tops---->  250/-\n ---Jeans---->  490/- \n----Sudi--->  450/-\n ----Saree---->  500/-")
    print("\n****Boys Season****\n----Shirts---->  450/-\n ---Jeans---->  550/- \n----Pants--->  400/-\n ")
    name=input("Enter Your Name:")
    Email_Id=input("Enter Your Mail Id:")
    current_date()
    try:

        print("1-> Girls season")
        print("2-> Boys Season")


        user=int(input("Enter Your Season Number:"))
        if user==1:
            stocks.Girls_Season()
        elif user==2:
            stocks.Boys_Season()
        else:
            print("thnak you")
    except:
        print("PLs enter numbers only")

main()