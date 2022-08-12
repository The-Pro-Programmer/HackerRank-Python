#https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true

from collections import Counter


x = int(input())
showSizes = Counter(map(int, input().split()))
n = int(input())
total = 0
for i in range(n):
    size , price = map(int, input().split())
    if showSizes[size] >0:
        showSizes[size] -= 1
        total += price
print(total)