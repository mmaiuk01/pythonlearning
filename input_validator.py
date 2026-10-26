# Student Profile Validator
# Collects four fields, checks every rule for every field, and reports ALL errors at once.

VALID_MAJORS = ["CS", "IT", "CE", "DS"]

# Requirement 1: collect all four inputs first
student_id = input("Enter student ID: ")
name = input("Enter full name: ")
age_text = input("Enter age: ")
major = input("Enter major: ")

# Requirement 3: one list collects every error message
errors = []

# --- Student ID: exactly 8 chars, first is a letter, remaining 7 are digits ---
if len(student_id) != 8:
    errors.append(f"Student ID must be exactly 8 characters (got {len(student_id)})")

# [:1] (instead of [0]) avoids an IndexError when the ID is empty
if not student_id[:1].isalpha():
    errors.append("Student ID must start with a letter")

# Checked separately from the length so every broken rule gets reported
if not student_id[1:].isdigit():
    errors.append("Student ID must have only digits after the first character")

# --- Name: not empty after stripping, at least 2 characters ---
clean_name = name.strip()
if clean_name == "":
    errors.append("Name cannot be empty")
elif len(clean_name) < 2:
    # elif: an empty name already has an error, so don't also report "too short"
    errors.append("Name must be at least 2 characters")

# --- Age: must be an integer (try/except), then between 16 and 99 inclusive ---
age = None
try:
    age = int(age_text)
except ValueError:
    errors.append("Age must be a valid integer")
else:
    # Only runs if int() succeeded, so the range check never sees non-numbers
    if age < 16 or age > 99:
        errors.append(f"Age must be between 16 and 99 (got {age})")

# --- Major: must be one of CS, IT, CE, DS (case-insensitive) ---
if major.strip().upper() not in VALID_MAJORS:
    errors.append(f"Major must be one of: {', '.join(VALID_MAJORS)} (got {major})")

# --- Requirement 4: report results ---
if not errors:
    print("\n Profile created successfully!")
    print(f"  Student ID: {student_id}")
    print(f"  Name: {clean_name}")
    print(f"  Age: {age}")
    print(f"  Major: {major.strip().upper()}")
else:
    print("\n Profile has errors:")
    for error in errors:
        print(f"  - {error}")

