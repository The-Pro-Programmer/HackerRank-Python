def average(array):
    heights = set(array)
    average = float(sum(heights)) / len(heights)
    return average

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
