#prompts for item price and sales tax from user
price = input("Enter the item price ($): ")
tax = input("Enter the sales tax (%): ")

#calculates total item price with sales tax added and prints result
totalCost = price + price * (tax/100)
print "The total cost is $",totalCost,"."