#https://www.hackerrank.com/challenges/polar-coordinates/problem?isFullScreen=true

from cmath import polar


num = complex(input())
z = complex(num)

print(polar(z)[0])
print(polar(z)[1])
