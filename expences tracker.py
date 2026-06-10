expenses = []
print("Welcome to the expense tracker")
while True:
  print("====MENU====")
  print("1. Add expense")
  print("2. View expenses")
  print("3. Total Amount")
  print("4. Exit")
  choice = input("Enter the choice: ")

  if choice == "1":
    amount = float(input("Enter the amount: "))
    expense = {
      "amount": amount
    }
    expenses.append(expense)

  elif choice == "2":
    print("Expenses")
    for expense in expenses:
      print(expense)

  elif choice == "3":
    total = sum(item["amount"] for item in expenses)
    print("Total Amount:", total)

  elif choice == "4":
    print("Exiting the expense tracker. Goodbye!")
    break
  else:
    print("Invalid choice. Please enter 1, 2, 3 or 4.")




