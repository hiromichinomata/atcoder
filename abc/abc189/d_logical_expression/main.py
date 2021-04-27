#!/bin/python3

import sys
# input = sys.stdin.readline
import math

if sys.platform =='ios':
	sys.stdin=open('input1.txt')

def main():
	n = list(map(int, input().strip().split()))[0]
	s = [0] * n
	for i in range(n):
		s[i] = list(map(str, input().strip().split()))[0]

	s = list(reversed(s))
	result = 1
	for i in range(n):
		if s[i] == 'OR':
			result += 2 ** (n-i)
	print(result)

main()
