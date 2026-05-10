initial_balance = 5000
correct_pin = 123

enter_pin = int(input("Enter your PIN: "))
if enter_pin == correct_pin:
    print("1.Withdraw")
    print("2.Check Balance")
    print("3.Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        amount = int(input("Enter the amount to withdraw: "))
        if amount > initial_balance:
            print("Insufficient balance")
        else:
            initial_balance -= amount
            print(f"Withdrawal successful. Remaining balance: {initial_balance}")
    elif choice == 2:
        print(f"Your current balance is: {initial_balance}")
    elif choice == 3:
        print("Thank you for using the ATM. Goodbye!")
    else:
        print("Invalid choice")