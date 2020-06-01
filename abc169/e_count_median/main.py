import math
import sys
input = sys.stdin.readline

def main():
  n = int(input().strip())
  item_list = []
  for i in range(n):
    item = list(map(int, input().strip().split()))
    item_list.append(item)

  item_list.sort(key=lambda x: x[0])

  if len(item_list) % 2 == 1:
    index = len(item_list) // 2
    result = item_list[index][1] - item_list[index][0] + 1
  else:
    index1 = len(item_list)//2 -1
    index2 = index1 + 1
    result = item_list[index2][1] - item_list[index1][0] + 1

  item_list.sort(key=lambda x: x[1])

  if len(item_list) % 2 == 1:
    index = len(item_list) // 2
    tmp = item_list[index][1] - item_list[index][0] + 1
    print(max(result, tmp))
  else:
    index1 = len(item_list)//2 -1
    index2 = index1 + 1
    tmp = item_list[index2][1] - item_list[index1][0] + 1
    print(max(result, tmp))

main()
