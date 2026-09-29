print("=== TEXT ANALYZER ===")

sentence = input("Enter a sentence: ")

total_chars = len(sentence)
chars_without_spaces = len(sentence.replace(" ", ""))
word_count = len(sentence.split())
vowel_count = sum(1 for char in sentence.lower() if char in "aeiou")
upper_version = sentence.upper()
lower_version = sentence.lower()
reverse_version = sentence[::-1]

starts_with_capital = "Yes" if sentence and sentence[0].isupper() else "No"
ends_with_punctuation = "Yes" if sentence and sentence[-1] in ".!?," else "No"

W = 35

print()
print("--- Analysis Results ---")
print(f"{'Total Characters (with spaces):':<{W}} {total_chars}")
print(f"{'Characters (without spaces):':<{W}} {chars_without_spaces}")
print(f"{'Number of words:':<{W}} {word_count}")
print(f"{'Number of vowels:':<{W}} {vowel_count}")
print(f"{'Uppercase version:':<{W}} {upper_version}")
print(f"{'Lowercase version:':<{W}} {lower_version}")
print(f"{'Reversed:':<{W}} {reverse_version}")
print(f"{'Starts with capital letter:':<{W}} {starts_with_capital}")
print(f"{'Ends with punctuation:':<{W}} {ends_with_punctuation}")
