s = input("Enter a string: ")

count = 0

for i in s:
    if i.lower() in "aeiou":
        count += 1

print("Number of vowels =", count)