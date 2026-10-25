"""

Requirements
1. Display this menu:
   ===== ATM MENU =====
   1. Check Balance
   2. Deposit Money
   3. Withdraw Money
   4. Exit
2. Check balance: Display the current balance.
3. Deposit money:
   - Ask the user for an amount.
   - Accept only positive amounts.
   - Add the amount to the current balance.
   - Display the updated balance.
4. Withdraw money:
   - Ask for the withdrawal amount.
   - Reject zero or negative amounts.
   - Reject withdrawals greater than the available balance.
   - Otherwise, deduct the amount and display the updated balance.
5. Exit: Display a goodbye message and stop the program.
6. Invalid menu choice: Display an error message and show the menu again.


# Example run:

===== ATM MENU =====
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit

Enter your choice: 1
Current Balance: ₹5000

Enter your choice: 2
Enter deposit amount: 1000
Deposit successful!
Current Balance: ₹6000

Enter your choice: 3
Enter withdrawal amount: 2000
Withdrawal successful!
Current Balance: ₹4000

Enter your choice: 4
Thank you for using our ATM!


Rules for your solution
- Use a while loop to keep the ATM running.
- Use if-elif-else to handle menu choices.
- Use variables to track the balance.
- Handle invalid numeric input using try-except.
- Do not use classes, functions, or external libraries yet. 
  Focus on the fundamentals.

"""

current_balance = 5000



while True:
    print("-" * 20)
    print("===== ATM MENU =====")
    
    print(f"1. Check Balance")
    print(f"2. Deposit Money")
    print(f"3. Withdraw Money")
    print(f"4. Exit")
    print("-" * 20)

    print("Enter your choice: ", end="")
    
    try:

        choice = int(input())

        if choice not in (1, 2, 3, 4):
            print("Invalid choice! you must choose 1, 2, 3 or 4 ", end="")
            continue

    except ValueError:
        print(f"Invalid choice input. Enter choice again: ", end="")
        continue


    
    """
    
    try-except : runtime exceptions handle karta hai.

    if-elif-else : conditions aur business rules check karta hai.

    while : code repeat karta hai.

    continue : current iteration skip karta hai.

    break : nearest loop se bahar nikalta hai.


    """
    print("-" * 20)
    # 1. check current balance
    if choice == 1:
        print(f"Current Balance: Rs. {current_balance}")
        continue

    elif choice == 2:
        print("Enter your amount to deposit: ", end="")
        while True:
            try:
                deposit_balance = int(input())

                if deposit_balance <= 0:
                    print("Invalid deposit balance! enter valid one: ", end="")
                    continue
                current_balance += deposit_balance
                break
            except ValueError:
                print(f"Invalid amount. Enter a number: ", end="")
                continue
        print(f"Amounnt Rs. {deposit_balance} Deposit Successful!")
        print(f"Current Balance: Rs. {current_balance}")
        print("+" * 40)

    elif choice == 3:
        print("hey you're means want to withdraw some money!")
        print("Enter amount you want to withdraw: ", end="")
        while True:
            try:
                withdraw_balance = int(input())


                if withdraw_balance <= 0:
                    print("Enter a positive withdrawal amount: ", end="")
                    continue

                
                if current_balance < withdraw_balance:
                    print("Insufficient balance! ")
                    print(f"Your current balance is: Rs. {current_balance}")
                    print("Enter withdrawal amount again: ", end="")
                    continue

                current_balance -= withdraw_balance

                print("Withdrawal Successful!")
                print(f"Current Balance: Rs. {current_balance}")

                break

                
            except ValueError:
                print(f"Invalid amount. Enter a number: ", end="")
                continue

        print("+" * 40)


    elif choice == 4:
        print("Thank you for using our ATM!")

        print("+" * 40)
        break

    