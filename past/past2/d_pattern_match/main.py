#!/bin/python3

import re
import sys
input = sys.stdin.readline
from itertools import product

def main():
  s = input().strip()
  s_uniq = list(set(s)) + ['.']
  result = 0

  for r in range(3):
    candidates = set()
    for candidate in product(s_uniq, repeat=r+1):
      c_s = ''.join(candidate)
      candidates.add(c_s)

    for c_s in candidates:
      m_result = re.search(re.compile(c_s), s)
      if m_result is not None:
        result += 1

  print(result)

main()
