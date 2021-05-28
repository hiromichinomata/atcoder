#!/bin/python3

import sys
# input = sys.stdin.readline
import math

if sys.platform =='ios':
	sys.stdin=open('input1.txt')

def main():
	a, b = list(map(int, input().strip().split()))
	result = []
	for i in range(1, max(a,b)+1):
		result.append(i)
	for i in range(1, min(a,b)+1):
		result.append(-i)
	result[-1] -= sum(result)
	if b > a:
		result = list(map(lambda x: str(-x), result))
	else:
		result = list(map(str, result))
	print(' '.join(result))

main()
