Name = input("Enter your name\n> ")
Address = input("Enter your address\n> ")
PhoneNum = input("Enter your phone number\n> ")

Width = int(input("Enter the lawn width in metres\n> "))
Length = int(input("Enter the lawn length in metres\n> "))
SqrMeters = Width * Length

LawnCareCost = 1
while True:
    Quality = input("Enter the quality of lawn service you wish for:\nNone - 1\nEconomy - 2"
                    "\nStandard - 3\nLuxury - 4\n> ")
    if Quality == "1":
        break
    elif Quality == "2":
        LawnCareCost = 0.45
        break
    elif Quality == "3":
        LawnCareCost = 0.8
        break
    elif Quality == "4":
        LawnCareCost = 1.15
        break
    else:
        print("Please enter a valid lawn quality service number, as indicated above.")

CostSqrMeters = round(SqrMeters * 0.5, 2)
LawnCareFactored = round(SqrMeters * LawnCareCost, 2)
TotalCost = round(CostSqrMeters + LawnCareFactored, 2)
TotalVatCost = round(TotalCost * 1.2, 2)

print(f"Name: {Name}\nAddress: {Address}\nPhone Number: {PhoneNum}\n"
      f"Area of Lawn to cover: {Length}m x {Width}m - {SqrMeters}m\n\n"
      f"Labour cost: £{CostSqrMeters}\n"
      f"Lawn care cost: £{LawnCareFactored}\n"
      f"Total cost: £{TotalCost}\n"
      f"Total Cost (+VAT): £{TotalVatCost}")
