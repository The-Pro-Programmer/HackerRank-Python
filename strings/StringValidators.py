if __name__ == '__main__':
    s = input()
    alnum = False
    alpha = False
    digits = False
    lower = False
    upper = False
    for ch in s:
        if ch.isalnum():
            alnum = True
        if ch.isalpha():
            alpha = True
        if ch.isdigit():
            digits = True
        if(ch.islower()):
            lower = True
        if (ch.isupper()):
            upper = True

    print(alnum)
    print(alpha)
    print(digits)
    print(lower)
    print(upper)