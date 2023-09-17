def recursiveMultiplication(c,d):
    i = 0
    prod = 0
    while i < d:
        prod += c
        i += 1
    return prod

x = int(input("Enter the number to be multiplied: "))
y = int(input("Enter the multiplier: "))
print(recursiveMultiplication(x,y))
