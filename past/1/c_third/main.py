#!/bin/python3

import sys

arr = list(map(int, input().strip().split()))
s_a = sorted(arr)
print(s_a[-3])
