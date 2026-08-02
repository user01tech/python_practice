#program to remove a particular character from a string
s = input("enter a string --> ")
term = input("enter the char you want to remove from the string --> ")
result = '' 
for i in s:
    if i != term:
        result = result +i
print(result)