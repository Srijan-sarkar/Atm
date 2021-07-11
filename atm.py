class Atm():
    def __init__(self,choice):
        self.choice = choice
    
    def start(self,choice):
            if (choice==1):
                print("Your balance is 50000")
            elif (choice == 2):
                Withdraw = int(input("Enter the number you need"))
                Balance = 50000-Withdraw
                print("You have successfully Withdrawn ",Withdraw)
                print("You have ",Balance," left")
            else:
                print("Enter a valid number")        



def main():
    Card_no = input("Enter your card number") 
    Password = input("Enter the password")
    Withdraw_or_Balance = int(input("Press 1 if you would you like to withdraw or Press 2 if you want to check your balance"))
    
    Attempt = Atm(Withdraw_or_Balance)
    Attempt.start(Withdraw_or_Balance)

main()