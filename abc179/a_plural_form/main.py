#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  s = list(map(str, input().strip().split()))[0]
  if s[-1]=="s":
    print(s+"es")
  else:
    print(s+"s")

main()
