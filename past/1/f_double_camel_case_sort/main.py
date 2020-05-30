#!/bin/python3

import sys

s = input().strip()

words = []
tmp = []
mode = "s"

for i in range(len(s)):
  if s[i].isupper():
    if mode == "s":
      tmp = [s[i]]
      mode = "m"
    else:
      tmp.append(s[i])
      mode = "s"
      words.append(''.join(tmp))
  else:
    tmp.append(s[i])

sorted_words = sorted(words, key=lambda x:x.lower())
print(''.join(sorted_words))
