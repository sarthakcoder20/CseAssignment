def letterFrequency(x):
    letters = sorted("".join((x.split())))
    cnt = dict.fromkeys(letters)
    for m in cnt.keys():
        count = 0
        for d in letters:
            if d == m:
                count +=1
            cnt[m] = count
    print(f"The count of each letter in the sentence is {cnt}.")

letterFrequency(input("Enter a sentence: ")) 