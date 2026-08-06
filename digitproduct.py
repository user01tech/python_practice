
current = int(input("Enter starting number (n): "))
t = int(input("Enter value of t: "))

while True:
    temp = current
    product = 1

    while temp > 0:
        digit = temp % 10

        if digit == 0:
            product = 0
            break

        product *= digit
        temp //= 10

    if product % t == 0:
        print("Smallest Number =", current)
        break

    current += 1