menu = """

[D] = deposit
[W] = withdrawal
[S] = statement
[Q] = quit

->     """

balance = 0
deposit = 0
withdrawal = 0
statement = ""

deposit_per_day = 3
withdrawal_per_day = 3


while True:

    option = input(menu)

    if option == "d":
        amount = float(input("how much is the deposit?: "))
        
        deposit_limit = 1000

        if 0 < amount <= deposit_limit:
            if deposit >= deposit_per_day:
                print("The times of deposits was reached today, try another day :) ")
                continue
            balance += amount
            statement += "US$" + str(amount) + "\n"
            deposit += 1
            print(f"Deposited: {amount}")
            print(f"Balance = US${balance}")
        else:
            print("Invalid deposit amount or exceeds deposit limit.")
    
    elif option == "w":
        withdr = float(input("how much is the withdrawal?: "))
        
        withdrawal_limit = 1000

        if balance >= withdr <= withdrawal_limit:
            if withdrawal >= withdrawal_per_day:
                print("The times of withdrawal was reached today, try another day :) ")
                continue
            balance -= withdr
            withdrawal += 1
            statement += "-US$" + str(withdr) + "\n"
            print(f"Withdrawal: {withdr}")
            print(f"Balance = US${balance}")
        else:
            print("Invalid withdrawal amount or exceeds withdrawal limit.")

    elif option == "s":
        print("=================STATEMENT=================")
        print("any transaction was made." if not statement else "")
        print(statement)
        print(f"Balance: {balance}")
        print("===========================================")

    elif option == "q":
        print("Goodbye!")        
        break  

    else:
        print("Invalid option. Please try again.")