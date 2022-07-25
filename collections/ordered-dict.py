from typing import OrderedDict


n = int(input())
records = OrderedDict()
for i in range(n):
    record = input().split()
    itemCount = record[-1]
    itemName = " ".join(record[:-1])
    if itemName in records:
        records[itemName] += int(itemCount)
    else:
        records[itemName] = int(itemCount)
for item, count in records.items():
    print(item, count)