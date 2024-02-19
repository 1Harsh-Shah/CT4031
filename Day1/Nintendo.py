nintendo = 250

money = int(input("How much cash do you have right now?: "))
Can_buy = money // nintendo
Extra = money - (Can_buy * 250)
Earn_more = 250 - Extra

if Can_buy < 0:
    print("You cant afford a single one")
else:
    print(f"you can afford {Can_buy} with that amount and you can buy one more for {Earn_more}")

