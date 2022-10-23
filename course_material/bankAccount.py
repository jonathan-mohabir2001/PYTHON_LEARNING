#Bank Application Midterm Project - Created by Jonathan M. 

#In order to run this program, I decided to create a class called account. 
# The functions within this program will be using information within the class. 

#Code will be pretty long, but I have kept it simple and easy to read.
 
class Account:
    def __init__(self,name, balance, pin):
      self.name = name
      self.balance = balance
      self.pin = pin
    name =  "Jonathan"
    balance = 84000
    pin = 1234
# Atrributes created for predefined values for all functions to refer to. 
    def getBalance(self):
        return self.balance
    # method to return the balance at all times. 
    def getName(self):
        return self.name
    # Method to return the name at all times.
    def getPin(self):
        return self.pin
    # Method to return the pin at all times.
    

#Function to show money within account
def showBalance():
    print("Your current balance is: $",Account.getBalance(Account))

#Function below to withdraw money from the users account. 
def withdrawMoney():
    print("How much would you like to withdraw?")
    print("1. $20")
    print("2. $40")
    print("3. $60")
    print("4. $80")
    print("5. $100")
    print("6. Custom Amount")
  # The user is given preset options to withdraw money, and their own amount to withdraw.

    withdraw = int(input("Please select an option: "))
    #local variable in order to store amount of money to withdraw.
    if withdraw == 1:
        if Account.getBalance(Account) >= 20:
            Account.balance = Account.getBalance(Account) - 20
            print("Your new balance is: $",Account.getBalance(Account))
        else:
            print("Insufficient Funds")
    #If the user selects 1, their balance is subtracted by 20. If there is not enough money, they do not have enough funds, and a message is outputted.
  
    elif withdraw == 2:
        if Account.getBalance(Account) >= 40:
            Account.balance = Account.getBalance(Account) - 40
            print("Your new balance is: $",Account.getBalance(Account))
        else:
            print("Insufficient Funds")
    #If the user selects 2, their balance is subtracted by 40. If there is not enough money, they do not have enough funds, and a message is outputted.
  
    elif withdraw == 3:
        if Account.getBalance(Account) >= 60:
            Account.balance = Account.getBalance(Account) - 60
            print("Your new balance is: $",Account.getBalance(Account))
        else:
            print("Insufficient Funds")
    #If the user selects 3, their balance is subtracted by 60. If there is not enough money, they do not have enough funds, and a message is outputted.
  
    elif withdraw == 4:
        if Account.getBalance(Account) >= 80:
            Account.balance = Account.getBalance(Account) - 80
            print("Your new balance is: $",Account.getBalance(Account))
        else:
            print("Insufficient Funds")
    #If the user selects 4, their balance is subtracted by 80. If there is not enough money, they do not have enough funds, and a message is outputted.
  
    elif withdraw == 5:
        if Account.getBalance(Account) >= 100:
            Account.balance = Account.getBalance(Account) - 100
            print("Your new balance is: $",Account.getBalance(Account))
        else:
            print("Insufficient Funds")
    #If the user selects 5, their balance is subtracted by 100. If there is not enough money, they do not have enough funds, and a message is outputted.
  
    elif withdraw == 6:
        customWithdraw = int(input("How much would you like to withdraw? "))
        if Account.getBalance(Account) >= customWithdraw:
            Account.balance = Account.getBalance(Account) - customWithdraw
            print("Your new balance is: $",Account.getBalance(Account))
        else:
            print("Insufficient Funds")
    #If the user selects 6, they are asked to input their own amount to withdraw. If there is not enough money, they do not have enough funds, and a message is outputted.
    else:
        print("Invalid Option")

#A function is created for the user to deposit money into their account.
def depositMoney():
    deposit = int(input("How much would you like to deposit? "))
    #local variable declared to store the amount of money to deposit.
    Account.balance = Account.getBalance(Account) + deposit
    #Balance will be updated with the new amount of money.
    print("Your new balance is: $",Account.getBalance(Account))
    #New balance will be outputted to the user. 
#ALL necessary functions are now created for the banking application.

#A main function is created below to run the program, parameters given from assignment are followed. 
def main():
    print("Welcome to TD/CIBC/Scotiabank/HSBC Bank")
    print("Please enter your pin to continue")
    #Welcome message to user, and they are asked to enter a pin. 
    attempts = 0
    #local variable declared in order to check for the attempts of pin entry.

    #The while loop is utilized to see the pin entry, the if statement is then nested to allow for the program to run after checking pin. 
    while attempts < 3:
        pin = int(input("Pin: "))
        if pin == Account.getPin(Account):
            print("Welcome",Account.getName(Account))
            print("What would you like to do?")
            print("1. View Balance")
            print("2. Withdraw Money")
            print("3. Deposit Money")
            print("4. Exit")
          #pre determined options are given for the user to their banking.

            option = int(input("Please select an option: "))
            if option == 1:
                showBalance()
            # If the user is 1 the created showBalance function is called. 
            elif option == 2:
                withdrawMoney()
            # If the user is created the withdrawMoney is called, this has it's 
            elif option == 3:
                depositMoney()
            elif option == 4:
                print("Thank you for using the banking application!")
                break
            # If the user is 4, the program will end.
            else:
                print("Invalid Option")
            # If the user does not select a valid option, they will be asked to select a valid option.
        else:
            print("Incorrect Pin")
            attempts = attempts + 1
            if attempts == 3:
                print("Too many attempts. Please try again later.")
                break
            # If the user enters the incorrect pin, they will be asked to try again. If they enter the incorrect pin 3 times, they will be asked to try again later.
            else:
                print("You have",3-attempts,"attempts left")
main()