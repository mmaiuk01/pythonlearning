# Shipping Cost Calculator

# First we ask user weith of the package and type of service
weight = float(input("Enter package weight (lbs): "))
service = input("Enter service (standart/express): ").strip().lower()

if weight <= 0:  # if weight 0 or less we stop
    print("Invalid weight.")
elif (
    service != "standart" and service != "express"
):  # if service is neither we also stop
    print("Invalid service.")
else:

    if weight <= 5:  # calculating the base cost
        cost = 5
    elif weight <= 20:
        cost = 5 + (weight - 5) * 0.75
    else:
        cost = 16.25 + (weight - 20) * 0.50


if service == "express":  # if service is express we charge 25% more
    cost = cost * 1.25

# Show results with two decimal places
print(f"Shipping cost: ${cost:.2f}")
