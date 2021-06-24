Card_no = input("Enter your card number") 
Password = input("Enter the password")
Withdraw_or_Balance = input("Would you like to withdraw or check your balance")
if Withdraw_or_Balance==1:
                print("Your balance is 50000")
elif Withdraw_or_Balance==2:
                Withdraw = input("Enter the number you need")
                Balance = 50000-Withdraw
                print("You have successfully Withdrawn ",Withdraw)
                print("You have ",Balance," left")
else:
                print("Enter a valid number") 

class Atm():
    
    
    def start():
            if Withdraw_or_Balance==1:
                print("Your balance is 50000")
            elif Withdraw_or_Balance==2:
                Withdraw = input("Enter the number you need")
                Balance = 50000-Withdraw
                print("You have successfully Withdrawn ",Withdraw)
                print("You have ",Balance," left")
            else:
                print("Enter a valid number")        

Attempt = Atm()

Attempt.start