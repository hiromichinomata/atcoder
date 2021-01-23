#!/bin/python3
# ref: https://marco-note.net/abc-188-work-log/

import sys
input = sys.stdin.readline
from itertools import accumulate

def main():
  n, C = list(map(int, input().strip().split()))
  events = []
  for _ in range(n):
    a, b, c = list(map(int, input().strip().split()))
    a -= 1
    events.append([a, b, c])

  # 座標圧縮
  day = set()
  for a, b, c in events:
      day.add(a)
      day.add(b)
  day = sorted(day)  # day[i]: 実日付を昇順に並べたリスト
  D = {}  # D[d]: 実日付-->dayのインデックスに対応づけるためのマップ
  for i, d in enumerate(day):
      D[d] = i
  L = len(day)  # L: dayの長さ

  events = sorted(events)

  S = [0] * L
  for a, b, c in events:
      S[D[a]] += c
      S[D[b]] -= c
  T = list(accumulate(S)) # T[i]: 期間i(day[i + 1] - day[i])における1日あたりの従量料金

  # 各期間iについて, 従量料金と定額料金を比較しどちらを採用するか決める。
  # 期間の長さ(=日数)は day[i + 1] - day[i] により計算できる。
  ans = 0
  for i in range(L - 1):
      cost = min(T[i], C)
      days = day[i + 1] - day[i]
      ans += cost * days
  print(ans)

main()
