#https://www.hackerrank.com/challenges/any-or-all/problem?isFullScreen=true

n = int(input())
nums = list(map(int, input().split()))
print(all([all(x>0 for x in nums), any(str(x)==str(x)[::-1] for x in nums)]))