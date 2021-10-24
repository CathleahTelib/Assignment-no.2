amount_of_money_you_have = int(input("How much is your money?:"))
applePrice = int(input("How much is the apple:"))

you_can_buy = amount_of_money_you_have // applePrice
your_change_is = amount_of_money_you_have % applePrice

print(f"You can buy {you_can_buy} apples and your change is {your_change_is}")
