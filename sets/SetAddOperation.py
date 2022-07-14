if __name__ == '__main__':
    n = int(input())
    countries = set()
    for i in range(0,n):
        country = input()
        countries.add(country)
    print(len(countries))
