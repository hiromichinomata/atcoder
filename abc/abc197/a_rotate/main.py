#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  s = list(map(str, input().strip().split()))[0]
  print(s[1] + s[2] + s[0])

main()
