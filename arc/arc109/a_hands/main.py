#!/bin/python3

import sys
# input = sys.stdin.readline

if sys.platform =='ios':
	sys.stdin=open('input1.txt')

def main():
	a, b, x, y = list(map(int, input().strip().split()))
	b -= a
	result = min(2*x, y) * b
	print(result)

main()
