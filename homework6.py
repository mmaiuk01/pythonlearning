# Loop Lecture 2 Unit 1 Exercise 2 Complete while loop
num = 1
while num <= 5:
    print(num)
    num += 1

print("End of first exercise.")

# Loop Lecture 2 Unit 1 Exercise 3 Convert for to while


num = 0
while num < 5:
    print(num)
    num += 1

print("End of second exercise.")
# Loop Lecture 2 Unit 2 Exercise 2 Trace and Fix
num = 2
while num <= 10:
    print(num)
    num += 2

print("End of third exercise.")

# Loop Lecture 2 Unit 2 Exercise 3 Doubling challenge
num = 1
count = 0

while num <= 1000:
    print(num)
    num *= 2
    count += 1
print(f"It took {count} doublings to exceed 1000.")

print("End of fourth exercise.")

# Loop Lecture 2 Unit 3 Exercise 2 Convert between two loops
num = 10
while num > 0:
    print(num)
    num -= 1
print("Converted.")
val = 1
for _ in range(10):
    val *= 2
    print(val)

print("Converted. End of fifth exercise.")

# Loop Lecture 2 Unit 3 Exercise 3 Design a menu system

choice = ""

while choice != "3":
    print("\nMenu:")
    print("1. Add two numbers")
    print("2. Subtract two numbers")
    print("3. Exit")

    choice = input("Choice your action (1-3): ")

    if choice == "1":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print(f"{a} + {b} = {a + b}")
    elif choice == "2":
        a = float(input("Enter greater number: "))
        b = float(input("Enter a subtraction number: "))
        print(f"{a} - {b} = {a - b}")
    elif choice == "3":
        print("Goodbye.")
    else:
        print("Pick number from 1-3!")

print("End of sixth exercise.")

# Loop Lecture 3 Unit 1 Exercise 1 Add a break
for i in range(10):
    print(i)
    if i == 5:
        break
print("end of seventh exercise.")

# Loop Lecture 3 Unit 1 Exercise 2 Search with break
numbers = [3, 7, 9, 2, 11, 4, 13]

for num in numbers:
    if num % 2 == 0:
        print(num)
        break
print("End of eight exercise.")


# Loop Lecture 3 Unit 1 Exercise 3 Password checker
correct_password = "secure123"

for attempt in range(3):
    guess = input("Enter password: ")
    if guess == correct_password:
        print("Access granted!")
        break
else:
    print("Account locked.")

print("End of ninth exrcise.")

# Loop Lecture 3 Unit 2 Exercise 1 Skip one number
for i in range(6):
    if i == 3:
        continue
    print(i)

print("End of tenth exercise.")

# Loop Lecture 3 Unit 2 Exercise 2 Filter data
scores = [85, -5, 92, 150, 78, 45, 200]
total = 0
count = 0

for score in scores:
    if score < 0 or score > 100:
        continue
    total += score
    count += 1

average = total / count
print(f"Average of valid scores: {average}")

print("End of eleventh exercise.")

# Loop Lecture 3 Unit 2 Exercise 3 Multiple skip conditions
words = ["hi", "xerox", "", "python", "xy", "code", "x", "algorithm"]

for word in words:
    if len(word) <= 2:
        continue
    if word.startswith("x"):
        continue
    print(word)
    