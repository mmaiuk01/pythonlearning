CURRENT_YEAR = 2026
BORDER_WIDTH = 40

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
birth_year = int(input("Enter your birth year: "))
hobby = input("Enter your hobby: ")

first_name = first_name.strip().title()
last_name = last_name.strip().title()
full_name = f"{first_name} {last_name}"
hobby = hobby.strip().title()

age = CURRENT_YEAR - birth_year

thick_border = "=" * BORDER_WIDTH
thin_border = "-" * BORDER_WIDTH

print()
print(thick_border)
print(f"{'USER PROFILE CARD':^{BORDER_WIDTH}}")
print(thick_border)
print(f"{'Full Name:':<8} {full_name}")
print(f"{'Age:':<8} {age}")
print(f"{'Hobby:':<8} {hobby}")
print(thin_border)
print("Thank you for creating your profile!")
print(thick_border)
