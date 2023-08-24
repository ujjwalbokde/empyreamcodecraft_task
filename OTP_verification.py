import random
import smtplib

sender_email=input("Enter your email : ")
Password = 'piirgpanacbaodmm'
receiver_email=input("Enter the email of receiver: ")
otp=random.randint(100000, 999999)
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

server.login(sender_email,Password)
server.sendmail(sender_email,receiver_email,f'Your OTP is {otp}.')
print("Email sent !")
verify=int(input("Enter otp sent to your email: "))

while True:
    if verify==otp:
        print("Verification successfull !")
        break
    else:
        print("Wrong OTP, Please try again")