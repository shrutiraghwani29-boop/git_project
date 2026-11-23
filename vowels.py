text = input("Enter a string: ")

vowels = "aeiouAEIOU"

for ch in text:
    if ch in vowels:
        print(ch)