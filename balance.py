balance=20000
correct_pin=1234

print("Welcome to the Global Bank ATM")
user_pin=int(input("Please enter your PIN: "))

if user_pin==correct_pin:
    print('1 Check Balance')
    print('2 Withdraw Money')
    print('3 Exit')
    
    choice=int(input("Please select an option: "))

    if choice==1:
        print(f'Your current balance is: Rs. {balance}')
    elif choice==2:
        amount=int(input("Enter the amount to withdraw: "))
        if amount<=balance:
            balance-=amount
            print(f'Please collect your cash. Your remaining balance is: Rs. {balance}')
        elif amount<0:
            print("Please enter a valid amount.")
        else:
            print("Insufficient balance.")

    elif choice==3:
        print("Thank you for using Global Bank ATM. Goodbye!")
    else:
        print("Invalid option selected.")
else:
    print("Incorrect PIN. Please try again.")
