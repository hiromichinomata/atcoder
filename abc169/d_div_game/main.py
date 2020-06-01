import math
import sys
input = sys.stdin.readline

def main():
  n = original_n = int(input().strip())
  max_search = int(math.sqrt(n)) + 1
  result = 0

  if n == 1:
    print("0")
    sys.exit()

  for i in range(2, max_search):
    if n % i == 0:
      result += 1
      n = n / i

    if n == 1:
      break

  if n == original_n:
    result += 1

  print(result)

main()
