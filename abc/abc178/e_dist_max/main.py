#!/bin/python3

import sys
# input = sys.stdin.readline

if sys.platform =='ios':
	sys.stdin=open('input1.txt')

def main():
	n = list(map(int, input().strip().split()))[0]
	plus = [0]*n
	minus = [0]*n
	for i in range(n):
		x, y = list(map(int, input().strip().split()))
		plus[i] = x+y
		minus[i] = x-y
	plus = sorted(plus)
	minus = sorted(minus)
	result = abs(plus[-1] - plus[0])
	result = max(result, abs(minus[-1]-minus[0]))
	
	print(result)

main()
