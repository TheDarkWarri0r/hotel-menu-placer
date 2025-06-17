menu = {
    'pizza': 450,
    'veg chaumein': 100,
    'chicken chaumein': 200,
    'veg momo': 90,
    'chicken momo': 150,
}

print('Welcome to Bakchodi Resort ("Bakchodi gar ni chill garni")')
print("Menu:")
for item, price in menu.items():
    print(f" {item.title()}: Rs{price}")

order_total = 0
order_list = []

while True:
    item = input("\nEnter the item you want to order: ").strip().lower()
    if item in menu:
        try:
            qty = int(input(f"How many plates of {item}? "))
            if qty > 0:
                cost = menu[item] * qty
                order_total += cost
                order_list.append((item, qty, cost))
                print(f"✅ Added {qty} x {item} = Rs{cost}")
            else:
                print("❌ Quantity must be greater than 0.")
        except ValueError:
            print("❌ Please enter a valid number.")
    else:
        print(f"❌ '{item}' is not available on the menu.")

    another = input("Do you want to add another item? (yes/no): ").strip().lower()
    if another != "yes":
        break

print("\n🧾 Your Order Summary:")
for item, qty, cost in order_list:
    print(f" - {qty} x {item.title()} = Rs{cost}")

print(f"\n💰 Total Amount: Rs{order_total}")

confirm = input("Do you want to confirm the order? (yes/no): ").strip().lower()
if confirm == "yes":
    print("🎉 Order placed! Thank you for ordering from Bakchodi Resort.")
else:
    print("❌ Order canceled.")