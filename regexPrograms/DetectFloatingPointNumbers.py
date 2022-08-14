#https://www.hackerrank.com/challenges/introduction-to-regex/problem?isFullScreen=true

import re


n = int(input())

for i in range(n):
    num = input()
    print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', num)))
