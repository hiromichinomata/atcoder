#!/bin/python3

import sys
# input = sys.stdin.readline
import math

if sys.platform =='ios':
	sys.stdin=open('input1.txt')

def main():
	x, y, a, b = list(map(int, input().strip().split()))
	result = 0
	l = int(math.log(y/x, a))
	for i in range(1, l+1):
		tmp = y-1-x*a**i
		print(i + tmp//b)
		result = max(result, i + tmp//b)
		
	print(result)

main()
