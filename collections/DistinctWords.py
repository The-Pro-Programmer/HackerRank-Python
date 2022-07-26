from typing import OrderedDict


n = int(input())
words = list()
for i in range(n):
    words.append(input())
wordsDict = OrderedDict()
for word in words:
    if word in wordsDict:
        wordsDict[word] += 1
    else:
        wordsDict[word] = 1
print(len(wordsDict))
print(" ".join(str(count) for item, count in wordsDict.items()))
