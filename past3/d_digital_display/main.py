#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n = int(input().strip())
  s = []
  for i in range(5):
    s.append(input().strip())

  num = ['.###..#..###.###.#.#.###.###.###.###.###',
        '.#.#.##....#...#.#.#.#...#.....#.#.#.#.#',
        '.#.#..#..###.###.###.###.###...#.###.###',
        '.#.#..#..#.....#...#...#.#.#...#.#.#...#',
        '.###.###.###.###...#.###.###...#.###.###']
  board = []
  for i in range(10):
    tmp = []
    for j in range(5):
      tmp.append(num[j][4*i:4*i+4])
    board.append(tmp)

  result = ''
  for k in range(n):
    for i in range(10):
      count = 0
      for j in range(5):
        if board[i][j] == s[j][4*k:4*k+4]:
          count += 1
        else:
          break
      if count == 5:
        result += str(i)
        break

  print(result)

main()
