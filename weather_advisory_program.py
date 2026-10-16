# Get input from the user
temp = float(input("Enter the current temperature in F: "))
rain_input = input("Is it raining? (yes/no): ").strip().lower()
raining = rain_input == "yes"

# Determine the weather advisory based on the input
if temp > 100:
    print("EXTREEME HEAT WARNING: Stay indoors!")

elif temp > 85 and raining:
    if raining:
        print("Warm rain — watch for flash floods.")
    else:
        print("Hot and dry — stay hydrated.")
elif temp >= 65:
    if raining:
        print("Grab an umbrella!")
    else:
        print("Nice weather — enjoy your day!")
elif temp >= 32:
    print("It's cold — bundle up!")
elif temp < 32:
    print("FREEZE WARNING: Roads may be icy!")
