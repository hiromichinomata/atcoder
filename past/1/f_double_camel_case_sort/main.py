#!/bin/python3

import sys

s = input().strip()

words = []
tmp = ""
mode = "start"

for i in range(len(s)):
  if s[i].isupper():
    if mode == "start":
      tmp = s[i]
      mode = "middle"
    else:
      tmp += s[i]
      mode = "start"
      words.append(tmp)
  else:
    tmp += s[i]

sorted_words = sorted(words, key=lambda x:x.lower())
print("".join(sorted_words))
