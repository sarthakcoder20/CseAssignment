def listSumUp():
    y = eval(input("Enter a list (with enclosing brackets): "))
    temp = list()
    sum = 0
    for i in range(0, len(y)):
        sum += int(y[i])
        temp.append(sum)
    return temp

print(listSumUp())
        