# Step 1: Ask user for three values
a = int(input("Enter value for a:"))
b = int(input("Enter value for b:"))
c = int(input("Enter value for c:"))

print()

# Step 2: Evaluate each expression and store the result

expr1 = a < b < c

expr2 = not (a > b or b > c)

expr3 = a <= b and b <= c

print()

print(f"a < b < c       : {expr1}")
print(f"not (a > b or b > c) : {expr2}")
print(f"a <= b and b <= c : {expr3}")

print()

# Step 3: Compare the results of the three expressions 2 and 3 to confirm De Morgans Law
if expr2 == expr3:
    print("De Morgans Law is confirmed: Expression 2 and Expression 3 are match!")
else:
    print("De Morgans Law is NOT confirmed: Expression 2 and Expression 3 differ.")
