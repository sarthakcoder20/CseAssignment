def stringReverser(o):
    reverse = ""
    for i in range(len(o)-1,-1,-1):
        reverse += o[i]
    return reverse

print(stringReverser(input("Enter a sentence: ")))