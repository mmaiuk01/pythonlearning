def is_palindrome(text):
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


word = input("Enter a word or phrase:")

if is_palindrome(word):
    print(f'"{word}" is a palindrome.')
else:
    print(f'"{word}" is not a palindrome.')
