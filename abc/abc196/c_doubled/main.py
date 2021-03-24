#!/bin/python3

import sys
# input = sys.stdin.readline

if sys.platform =='ios':
	sys.stdin=open('input1.txt')

def main():
	n = list(map(int, input().strip().split()))[0]
	result = 0
	for i in range(1, int(10**(len(str(n))/2)+1)):
		if i * 10**len(str(i)) + i > n:
			break
		result += 1
	print(result)

main()
