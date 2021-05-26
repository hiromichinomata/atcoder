#!/bin/python3

import sys
# input = sys.stdin.readline
import math

if sys.platform =='ios':
	sys.stdin=open('input1.txt')

def main():
	n = list(map(int, input().strip().split()))[0]
	result = 1
	for i in range(2, n+1):
		result = result * i // math.gcd(result, i)
	print(result+1)

main()
