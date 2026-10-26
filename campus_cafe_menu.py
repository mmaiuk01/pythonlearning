# Campus Cafe Order System
# Menu-driven program: shows a menu, handles customizations with nested if
# statements, validates all input, and prints a formatted receipt.

TAX_RATE = 0.07
LINE = "=" * 32

# ---- Display the menu ----
print(LINE)
print("     CAMPUS CAFE ORDER SYSTEM")
print(LINE)
print("  1. Coffee      - $3.50")
print("  2. Sandwich    - $6.00")
print("  3. Salad       - $5.50")
print("  4. Combo       - $8.00")
print("  5. Exit")
print(LINE)

choice = input("Enter your choice (1-5): ").strip()

# Outer level: which menu item was chosen. Inner level: its customizations.
if choice == "5":
    print("Goodbye!")

elif choice in ("1", "2", "3", "4"):
    item_name = ""
    unit_price = 0.0

    if choice == "1":
        # Coffee: ask for size
        item_name = "Coffee"
        unit_price = 3.50
        size = input("Size (small/medium/large): ").strip().lower()
        if size == "medium":
            unit_price += 1.00
            item_name += " (Medium)"
        elif size == "large":
            unit_price += 2.00
            item_name += " (Large)"
        elif size == "small":
            item_name += " (Small)"
        else:
            # Invalid size defaults to Small with a message
            print("Invalid size. Defaulting to Small.")
            item_name += " (Small)"

    elif choice == "2":
        # Sandwich: ask about cheese
        item_name = "Sandwich"
        unit_price = 6.00
        cheese = input("Add cheese? (yes/no): ").strip().lower()
        if cheese == "yes":
            unit_price += 0.75
            item_name += " + Cheese"

    elif choice == "3":
        # Salad: ask for dressing (case-insensitive)
        item_name = "Salad"
        unit_price = 5.50
        dressing = input("Dressing (ranch/italian/vinaigrette/none): ").strip().lower()
        if dressing in ("ranch", "italian", "vinaigrette"):
            item_name += " (" + dressing.capitalize() + " dressing)"
        elif dressing == "none":
            pass
        else:
            # Invalid dressing defaults to none with a message
            print("Invalid dressing. Defaulting to none.")

    else:
        # Combo: apply BOTH the coffee size and the cheese customizations
        item_name = "Combo (Sandwich + Coffee)"
        unit_price = 8.00
        size = input("Coffee size (small/medium/large): ").strip().lower()
        if size == "medium":
            unit_price += 1.00
            item_name += ", Medium"
        elif size == "large":
            unit_price += 2.00
            item_name += ", Large"
        elif size == "small":
            item_name += ", Small"
        else:
            print("Invalid size. Defaulting to Small.")
            item_name += ", Small"
        cheese = input("Add cheese? (yes/no): ").strip().lower()
        if cheese == "yes":
            unit_price += 0.75
            item_name += ", Cheese"

    # ---- Student name: cannot be empty ----
    name = input("Enter your name: ").strip()
    if name == "":
        print("Error: name cannot be empty.")
    else:
        # ---- Quantity: must be a positive integer (try/except) ----
        try:
            quantity = int(input("How many? "))
        except ValueError:
            print("Error: quantity must be a whole number.")
        else:
            if quantity <= 0:
                print("Error: quantity must be positive.")
            else:
                # ---- Totals ----
                subtotal = unit_price * quantity
                tax = subtotal * TAX_RATE
                total = subtotal + tax

                # ---- Receipt ----
                print()
                print(LINE)
                print("          ORDER RECEIPT")
                print(LINE)
                print(f"Customer:   {name}")
                print(f"Item:       {item_name}")
                print(f"Quantity:   {quantity}")
                print(f"Unit Price: ${unit_price:.2f}")
                print(f"Subtotal:   ${subtotal:.2f}")
                print(f"Tax (7%):   ${tax:.2f}")
                print(f"Total:      ${total:.2f}")
                print(LINE)
                print("Thank you for your order!")

else:
    print("Invalid choice. Please run the program again and enter 1-5.")
