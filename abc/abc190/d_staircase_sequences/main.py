#!/bin/python3

import sys
input = sys.stdin.readline

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    return arr

def main():
  n = list(map(int, input().strip().split()))[0]
  factored = factorization(n)
  count = 1
  for f in factored:
    i, j = f
    if i == 2:
        continue
    count *= (j+1)

  print(count*2)

main()
