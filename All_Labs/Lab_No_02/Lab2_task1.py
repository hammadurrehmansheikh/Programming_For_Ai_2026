food = 600
transport = 400
stationery = 200


total_expense = food + transport + stationery


budget = 1500


print("Food Expense:", food, "PKR")
print("Transport Expense:", transport, "PKR")
print("Stationery Expense:", stationery, "PKR")
print("Total Expense:", total_expense, "PKR")


if total_expense > budget:
    print("Budget Exceeded!")
else:
    print("Within Budget!")