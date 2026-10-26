# Calculates a ticket price based on the age of the customer and whether the showing is a matinee.

# First requirement: ask for age

age = int(input("Enter your age: "))

# Fifth requirement is to validate that age is non-negative
if age < 0:
    print("Error: age cannot be negative. Please enter a valid age.")
else:
    # Second requirement: ask if the showing is a matinee
    is_matinee = input("Is this a matinee showing? (yes/no): ").strip().lower()

# Fourth requirement is to convert ternary expression yes/no into a Boolean
is_matinee = True if is_matinee == "yes" else False

# Third Requirement: outer if/elif picks the age group, inner if/elif picks the price based on whether it is a matinee or not
if age < 13:
    age_group = "Child"
    if is_matinee:
        price = 6.00
    else:
        price = 8.00
elif age <= 17:
    age_group = "Teen"
    if is_matinee:
        price = 7.00
    else:
        price = 10.00
elif age <= 64:
    age_group = "Adult"
    if is_matinee:
        price = 8.00
    else:
        price = 13.00
else:
    age_group = "Senior"
    if is_matinee:
        price = 6.00
    else:
        price = 7.00

# Requirement 6: print the age group and price with two decimal places
print(f"Age group: {age_group} ")
print(f"Ticket price: ${price:.2f}")
