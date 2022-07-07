def is_leap(year):
    leap = year % 400 == 0

    return leap


year = int(input())
print(is_leap(year))