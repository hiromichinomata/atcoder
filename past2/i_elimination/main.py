#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n = int(input().strip())
  a = list(map(int, input().strip().split()))
  result = [0]*len(a)
  battle = [0]*len(a)

  for i in range(len(a)):
    battle[i] = (i, a[i])

  battle_count = 0
  while len(battle) > 1:
    battle_new = []
    battle_count += 1
    for i in range(0, len(battle)-1, 2):
      a = battle[i]
      b = battle[i+1]
      a_i, a_s = a
      b_i, b_s = b
      result[a_i] = battle_count
      result[b_i] = battle_count

      if a_s > b_s:
        battle_new.append(a)
      else:
        battle_new.append(b)

    battle = battle_new

  for i in result:
    print(i)

main()
