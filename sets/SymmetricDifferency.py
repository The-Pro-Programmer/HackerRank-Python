lena = int(input())
a = set(map(int, input().split()))
lenb = int(input())
b = set(map(int, input().split()))

adiffb = a.symmetric_difference(b)
adiffb = sorted(adiffb)
for num in adiffb:
    print(num)
