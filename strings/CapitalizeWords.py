#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    words = s.split()
    for word in words:
        s = s.replace(word, word.capitalize())
    return s

print(solve('elon musk'))