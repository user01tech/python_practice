# wap to find the frequuency of a character in a string
s = input("enter a string --> ")
term = input ("enter gthe character to find the frequency --> ")
counter = 0
for i in s:
    if i == term:
        counter += 1
print("the frequency of the character is --> ",counter)

