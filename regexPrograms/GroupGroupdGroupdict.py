#https://www.hackerrank.com/challenges/re-group-groups/problem?isFullScreen=true

import re


pattern = r"([a-zA-Z0-9])\1+"
matches = re.search(pattern, input())
if(matches) :
    print(matches.group(1))
else:
    print(-1)
