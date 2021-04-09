#!/bin/python3

import sys
# input = sys.stdin.readline

if sys.platform =='ios':
  sys.stdin=open('input1.txt')

def main():
  n = list(map(str, input().strip().split()))[0]
  nums = [int(n[i]) for i in range(len(n))]
  sum_num = sum(nums)%3

  arr = [0]*3
  for num in nums:
    arr[num%3] += 1

  if len(nums) == 1:
    if sum_num != 0:
      print(-1)
      sys.exit()

  if sum_num == 0:
    print(0)
    sys.exit()
  elif sum_num == 1:
    if arr[1] > 0:
      print(1)
    else:
      if len(n) ==2:
        print(-1)
        sys.exit()
      print(2)
  else:
    if arr[2] > 0:
      print(1)
    else:
      if len(n) ==2:
        print(-1)
        sys.exit()
      print(2)

main()
