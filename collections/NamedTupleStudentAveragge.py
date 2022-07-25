n = int(input())
headers = input().split()
markIndex = 0
for i in range(0, len(headers)):
    if(headers[i]=='MARKS'):
        markIndex = i
        break;
total = 0
for i in range(n):
    total += int(input().split()[markIndex])
total /= n
print('%.2f' %total)