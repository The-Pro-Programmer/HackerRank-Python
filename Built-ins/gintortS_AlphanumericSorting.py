#https://www.hackerrank.com/challenges/ginorts/problem?isFullScreen=true

from cgitb import reset


S = input()

loweCaseChars = []
upperCaseChars = []
numericOddChars = []
numericEvenChars = []

for ch in S:
    if(ch.isupper()):
        upperCaseChars.append(ch)
    elif(ch.islower()):
        loweCaseChars.append(ch)
    elif(ch.isnumeric):
        if(int(ch)%2==0):
            numericEvenChars.append(ch)
        else:
            numericOddChars.append(ch)

result = ''.join(ch for ch in sorted(loweCaseChars))
result += ''.join(ch for ch in sorted(upperCaseChars))
result += ''.join(ch for ch in sorted(numericOddChars))
result += ''.join(ch for ch in sorted(numericEvenChars))
print(result)
