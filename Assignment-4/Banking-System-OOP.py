class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amt):
        self.balance += amt
        print(f"{amt} deposited successfully")

class SavingsAccount(Account):
    def withdraw(self, amt):
        if amt > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amt
            print(f"{amt} withdrawn successfully")

    def show_balance(self):
        print(f"Current Balance: {self.balance}")



acc = SavingsAccount(1000)


while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amt = int(input("Enter amount to deposit: "))
        acc.deposit(amt)

    elif choice == "2":
        amt = int(input("Enter amount to withdraw: "))
        acc.withdraw(amt)

    elif choice == "3":
        acc.show_balance()

    elif choice == "4":
        break

    else:
        print("Invalid choice")
