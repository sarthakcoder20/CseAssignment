def anagram(c,d):

    str1 = sorted("".join(tuple(c.split())))
    str2 = sorted("".join(tuple(d.split())))
    
    if str1 == str2:
        return True
    else:
        return False

p = input("Enter a string: ")
q = input("Enter an anagram: ")

print(anagram(p,q))