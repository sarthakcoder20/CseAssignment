def numberToText(number):
    digStr = {
        "0":'zero',
        "1":"one",
        "2":"two",
        "3":"three",
        "4":"four",
        "5":"five",
        "6":'six',
        "7":'seven',
        "8":'eight',
        "9":"nine"
    }
    display = ""
    for h in number:
        display += digStr[h] + " "
    print(display)

y = input("Enter a number: ")
numberToText(y)