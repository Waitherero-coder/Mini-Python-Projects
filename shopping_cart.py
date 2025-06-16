print("These are the items available today:")

cart = {
    "milk": 61,
    "bread": 55,
    "eggs": 20,
    "rice": 100,
    "beans": 80
}

for item, price in cart.items():
    print(f"{item.title()}@ Ksh.{price}")

inquiry = input("\nWhat would you like to purchase? ")

if inquiry.lower() in cart:
    total = cart[inquiry.lower()]
    print(f"{inquiry.lower()} costs Ksh.{total}")
else:
    print("Sorry, that item is not available.")




