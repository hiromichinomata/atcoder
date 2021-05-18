#!/bin/python3

import sys
input = sys.stdin.readline

from itertools import product

def main():
  s = list(map(str, input().strip().split()))[0]
  result = 0

  for num in product('0123456789', repeat=4):
    num = list(num)
    flag = True
    for i in range(len(s)):
      if s[i] == 'o' and str(i) not in num:
        flag = False
        break
      elif s[i] == 'x' and str(i) in num:
        flag = False
        break
    if flag == True:
      result += 1

  print(result)

main()
