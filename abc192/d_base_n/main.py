#!/bin/python3

import sys
input = sys.stdin.readline
import math

def convert(s, n):
  result = 0
  s_i = list(reversed([int(char) for char in str(s)]))
  for i in range(len(s_i)):
    result += s_i[i] * (n**i)
  return result

def main():
  x = list(map(str, input().strip().split()))[0]
  m = list(map(int, input().strip().split()))[0]

  d = int(sorted([char for char in str(x)], reverse=True)[0])
  if len(x) >= len(str(m)):
    max_d = 10
    result = 0
    for i in range(d+1, max_d):
      converted = convert(x, i)
      if converted <= m:
        result += 1
  else:
    max_d = math.ceil(m / int(x) * 10)
    result = 1
    for i in range(max_d, d, -1):
      converted = convert(x, i)
      if converted <= m:
        result = i - d
        break

  print(result)

main()

# ## 22
# 3進数
# 2 * 3 + 2

# 4進数
# 2* 4 + 2

# ## 999
# 10進数
# 9 * 10**2 + 9 * 10**1 + 9

# 11進数
# 9 * 11**2 + 9 * 11**1 + 9
