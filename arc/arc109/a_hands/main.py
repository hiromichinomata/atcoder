#!/bin/python3

import sys
# input = sys.stdin.readline

if sys.platform =='ios':
	sys.stdin=open('input1.txt')

def main():
	a, b, x, y = list(map(int, input().strip().split()))
	d = abs(b-a)
	result = min(2*x, y) * d
	if a <= b:
		result += x
	else:
		if 2*x <= y:
			result -= x
		else:
			result +=x-y

	print(result)

main()
