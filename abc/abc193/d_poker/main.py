#!/bin/python3

import sys
input = sys.stdin.readline
from collections import defaultdict

def main():
  k = list(map(int, input().strip().split()))[0]
  s = list(map(str, input().strip().split()))[0]
  t = list(map(str, input().strip().split()))[0]

  takahashi_cards = [int(char) for char in s[:-1]]
  aoki_cards = [int(char) for char in t[:-1]]

  decks = defaultdict(int)
  for i in range(1, 10):
    decks[i] = k

  takahashi = defaultdict(int)
  aoki = defaultdict(int)

  for card in takahashi_cards:
    decks[card] -= 1
    takahashi[card] += 1

  for card in aoki_cards:
    decks[card] -= 1
    aoki[card] += 1

  takahashi_point = 0
  aoki_point = 0
  for i in range(1, 10):
    takahashi_point += i * 10 ** takahashi[i]
    aoki_point += i * 10 ** aoki[i]


  result = 0
  for i in range(1, 10):
    for j in range(1, 10):
      if (decks[i] >= 1 and decks[j] >= 1) or (i == j and decks[i] >= 2):
        new_takahashi_point = takahashi_point - (i * 10**takahashi[i]) + (i * 10**(takahashi[i]+1))
        new_aoki_point = aoki_point - (j * 10**aoki[j]) + (j * 10**(aoki[j]+1))
        if new_takahashi_point > new_aoki_point:
          total = 9 * k - 8
          probability = decks[i] / total
          total -= 1
          if i == j:
            probability *= (decks[j] - 1) / total
          else:
            probability *= decks[j] / total
          result += probability

  print(result)

main()
