#https://www.hackerrank.com/challenges/python-sort-sort/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    chart = list()

    for _ in range(n): 
        records = list(map(int, input().rstrip().split()))
        record = dict()
        for i in range(0, m):
            record[str(i)] = records[i]
        chart.append(record)

    k = input()

    chart = sorted(chart, key = lambda item : item[k])

    print('\n'.join(str(' '.join(str(val) for val in item.values())) for item in chart))



