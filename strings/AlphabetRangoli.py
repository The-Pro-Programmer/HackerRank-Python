from string import ascii_lowercase


def print_rangoli(size):
    alphabets = ascii_lowercase[:size]
    alphabets = alphabets[::-1]
    patterns = []
    maxsize = 0
    for i in range(0, size):
        pattern = '-'.join(alphabets[0:i] + alphabets[i] + alphabets[0:i][::-1])
        if(maxsize<len(pattern)):
            maxsize = len(pattern)
        patterns.append(pattern)
    for i in range(0, size):
        print(patterns[i].center(maxsize, '-'))
    for i in range(size-2, -1, -1):
        print(patterns[i].center(maxsize, '-'))

if __name__ == '__main__':
    for n  in range (3, 7):
        print_rangoli(n)