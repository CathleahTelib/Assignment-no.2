print("The price of the apple is 20 pesos")
apples= 20
print("The price of the oranges is 25 pesos")
oranges= 25

quantity_of_the_apple = int(input("How many apples would you like to purchase?:"))
quantity_of_the_orange = int(input("How many oranges would you like to purchase?:"))

applesAmount = apples * quantity_of_the_apple
orangesAmount= oranges * quantity_of_the_orange
amount = applesAmount + orangesAmount

print(f"The total amount is {amount}.")