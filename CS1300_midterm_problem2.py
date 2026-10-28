# Name Formatter
full_name = input("Enter your full name (2 or 3 words): ")

full_name = full_name.strip()   # Remove leading and trailing spaces
if full_name == "":
    print("No name entered.")
else:
    words = full_name.split()

    if len(words) != 2 and len(words) != 3:
        print("Please enter 2 or 3 names.")
    else:
        words = [w.capitalize() for w in words]     # Capitalize each word (first letter uppercase, rest lowercase)

        if len(words) == 2:
            first, last = words
            print("Formatted: " + last + ", " + first)
        else:
            first, middle, last = words
            print("Formatted: " + last + ", " + first + " " + middle)

        
        initials = ""   # Initials in the order the name was entered
        for i in words:
            initials += i[0].upper() + "."
        print("Initials: " + initials)