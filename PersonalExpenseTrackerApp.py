print("Personal Expense Tracker App")
Food = 0.0
Transport = 0.0
Bills = 0.0
Shopping = 0.0
Others = 0.0

while True:
    print("\n Choose an option")
    print("Add Expense")
    print("Show Summary")
    print("Data Export")
    print("Exit")

    Choice = input("\n Enter your Choice :")

    match Choice:
        case "1":
            print("\n Categories : Food, Transport,Bills,Shopping ,Others")
            Category = input("Enter Categopry :")
            Amount = float(input("Enter Amount : "))
            
            if Category == "Food":
                Food = Food + Amount
            elif Category == "Transport":
                Transport = Transport + Amount
            elif Category == "Bills":
                Bills = Bills + Amount
            elif Category == "Shopping":
                Shopping = Shopping + Amount
            else:
                Others = Others + Amount

            Total = Food + Transport + Bills + Shopping + Others
            print("Added",Amount,"To",Category,"Category")
        case "2":
            print("Show Summary ")
            print(f"Food",Food)
            print(f"Transport",Transport)
            print(f"Bills",Bills)
            print(f"Shopping ",Shopping)
            print(f"Others ",Others)
            print(f"Total Expense",Total)

            if Total >500:
                print("Warning ! You have spent more than 500 in this month")
            elif Total == 0 :
                print("You have not added any expense yet")
            else:
                print("You are managing your budget wisely ")

        case "3":
            print("Data Export ")

        case "4":
            print("Exit...")
            break

        case _ :
            print("Invalid Input")












