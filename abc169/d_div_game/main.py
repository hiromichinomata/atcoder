import math
import sys
input = sys.stdin.readline

"""nを素因数分解"""
"""2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""

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

    if arr==[]:
        arr.append([n, 1])

    return arr

def main():
  n = original_n = int(input().strip())
  factored = factorization(n)
  result = 0

  if n == 1:
    print("0")
    sys.exit()

  for i, count in factored:
    diff = 1
    while count > 0:
      count -= diff
      if count >= 0:
        result += 1
        diff += 1

  print(result)

main()
