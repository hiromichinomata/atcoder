#!/bin/python3

import sys
# input = sys.stdin.readline
from collections import defaultdict

if sys.platform =='ios':
  sys.stdin=open('input1.txt')

def main():
  s = list(map(str, input().strip().split()))[0]
  if len(s) < 3:
    if int(s) % 8 == 0:
      print('Yes')
      sys.exit()
    elif int(s[::-1]) % 8 == 0:
      print('Yes')
      sys.exit()
    else:
      print('No')
      sys.exit()
  
  nums = [int(char) for char in s]
  counts = defaultdict(int)
  for num in nums:
    counts[num] += 1
  for i in range(104, 1001, 8):
    candidate = [int(char) for char in str(i)]
    c_counts = defaultdict(int)
    for num in candidate:
      c_counts[num] += 1
    result = True
    for k,v in c_counts.items():
      if counts[k] < v:
        result = False
        break
    if result:
      print('Yes')
      sys.exit()

  print('No')

main()
