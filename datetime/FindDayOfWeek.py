import datetime

[mm, dd, yyyy] = list(map(int, input().split()))
now = datetime.datetime(yyyy, mm, dd)
print(now.strftime("%A").upper())