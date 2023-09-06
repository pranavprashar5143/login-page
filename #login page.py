#login page 
from getpass import getpass
username=input("enter username:")
password=getpass("enter password:")
print("            captcha:JY43d")
captcha=input("enter the captcha ")
captch="JY43d"
un="pranavprashar"
pw="pranav123"
if captcha==captch:
   print("captcha verified")
else:
     print("captcha is not verified")

if  password==pw and username==un and captcha==captch:
   print("enter the otp sent to your registered phone number")
   getpass("enter the otp")
   print("login successfully")
   print('''

                                 select your options:
                                1.All Options Of ATM
                                2.Profiles Details
                                3.Add New Account
                                4.Modify
                                5.Invoice''')
else:
     print("entered captcha,or username password is wrong")




