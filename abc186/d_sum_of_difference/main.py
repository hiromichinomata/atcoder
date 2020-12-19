# pypy3

import sys
input = sys.stdin.readline

def main():
  n = int(input().strip())
  a = list(map(int, input().strip().split()))
  a = sorted(a, reverse=True)
  result = 0
  num = len(a)-1
  for i in range(len(a)):
    result += num * a[i]
    num -= 2
  print(result)

main()
