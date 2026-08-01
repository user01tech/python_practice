# Program to check palindrome numbers

s = input("enter a number ")

if s == s[::-1]:
    print("palindrome")
else:
    print("not palindrome")
