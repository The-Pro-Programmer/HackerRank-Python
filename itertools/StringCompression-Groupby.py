from itertools import groupby


s = input()
chars = [int(i) for i,j in groupby(s)]
count = [len(list(j)) for i,j in groupby(s)]
result = ''
for i in range(0, len(chars)):
    result += ('(' + str(count[i])+ ', ' + str(chars[i]) + ') ')
print(result)

