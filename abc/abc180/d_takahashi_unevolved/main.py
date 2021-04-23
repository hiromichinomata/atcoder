#!/bin/python3

import sys
# input = sys.stdin.readline
import math

if sys.platform =='ios':
	sys.stdin=open('input1.txt')

def main():
	x, y, a, b = list(map(int, input().strip().split()))
	result = 0

	while x*a < x+b and x*a < y:
		x *= a
		result += 1
	result += (y-1-x)//b
		
	print(result)

main()
