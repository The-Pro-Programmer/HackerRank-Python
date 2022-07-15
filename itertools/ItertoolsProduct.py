#https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=true

from itertools import product


list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
result = ''
for item in product(list1, list2):
    result += str(item) + ' '
print(result)