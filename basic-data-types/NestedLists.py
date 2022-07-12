#https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == '__main__':
    records = []
    scores = []
    names = []
    n = int(input())
    for _ in range(n):
        name = input()
        score = float(input())
        records.append([name, score])
        scores.append(score)

    secondLowest = sorted(list(set(scores)))[1]

    records.sort()

    for name,score in records:
        if score==secondLowest:
            print(name)


