#!/bin/python3

import sys
# input = sys.stdin.readline
import math

if sys.platform =='ios':
	sys.stdin=open('input1.txt')

def main():
	r, x, y = list(map(int, input().strip().split()))
	d = (x**2 + y**2)**0.5
	if d < r:
		print(2)
		sys.exit()
	result = math.ceil( d / r )
	print(result)
		
main()
