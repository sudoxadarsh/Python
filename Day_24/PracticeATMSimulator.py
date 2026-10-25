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

# note: Sometimes i got distract & miss some logic i have to work on that.

choice = 0
currentBalance = 5000

while True:
    print("===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    print("Enter your choice: ", end="")
    try:
        choice = int(input())

        if choice not in (1, 2, 3, 4):
            print("Choose only 1, 2, 3, or 4 options :")
            continue


    except ValueError:
        print("Invalid value. Try again! : ")
        continue


    if choice == 1:
        print(f"Current Balance: rs. {currentBalance}")
        continue

    elif choice == 2:
        print("Enter amount to Deposit Money: ", end="")
        while True:
            try: 
                depositMoney = int(input())

                if depositMoney <= 0:
                    print("Please positive amount to deposit: ", end="")
                    continue
                
                currentBalance += depositMoney
                break

            except ValueError:
                print("Invalid input. Try again! :", end="")
                continue


        print("Deposit successful!")
        print(f"Current Balance: rs. {currentBalance}")

    elif choice == 3:
        print("Enter amout for withdrawal: ", end="")
        while True:
            try:
                withdrawMoney = int(input())

                if withdrawMoney <= 0:
                    print("Try again enter non zero positive amount to withdraw: ", end="")
                    continue

                # i forgot this logic to implement after a code review i make it here    
                if withdrawMoney > currentBalance:
                    print("Insufficient Balance.")
                    print(f"Current Balance: rs. {currentBalance}")
                    print("Again enter withdrawal amount: ", end="")
                    continue


                currentBalance -= withdrawMoney

                break

            except ValueError:
                print("Invalid input. Try again! :", end="")
                continue

        print("WIthdrawal successful!")
        print(f"Current Balance: rs. {currentBalance}")

    elif choice == 4:
        print("Thank you fo choosing our service!")
        break