expenses = {}
file_name = "expenses.txt"

try:
    with open(file_name, "r") as file:
        for line in file:
            category, amount = line.strip().split(",")
            expenses[category]=float(amount)
except FileNotFoundError:
    pass


def save_data():
    with open(file_name, "w") as file:
        for category, amount in expenses.items():
            file.write(f"{category},{amount}\n")


while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Delete Expense")
    print("5. Exit")

    choice = input("Enter your choice: ")
    
    if choice=="1":
        name=input("Enter the name : ")
        n=float(input("Enter that  expense: "))
        expenses[name]=n
        print("Expense added Successfully")
        save_data()
    elif choice=="2":
        if expenses:
            for name,n in expenses.items():
                print(f"Name:{name}||Expense:{n}")
        else:
            print("No expenses are found")
    elif choice=="3":
            Total=sum(expenses.values())       
            print("The Total expense is :",Total)
    elif choice=="4":
        name=input("Enter the name of the expense that need to be deleted: ")
        if name in expenses:
            del expenses[name]
            print("The Expense is deleted successfully")
            save_data()
        else:
            print("The name is not found")
    elif choice=="5":
        break
    
    else:
        print("Invaild choice")