#https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true

from math import asin, degrees, hypot, sqrt, cos, sin

if __name__ == '__main__':
    ab = int(input())
    bc = int(input())
    ca = hypot(ab,bc)
    mc = ca/2
    bca = asin(1*ab/ca)
    bm = sqrt((bc**2+mc**2)-(2*bc*mc*cos(bca)))
    mbc = asin(sin(bca)*mc/bm)
    print(int(round(degrees(mbc),0)),'\u00B0',sep='')

