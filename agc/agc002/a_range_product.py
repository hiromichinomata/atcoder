#!/bin/python3

import sys
# input = sys.stdin.readline

if sys.platform =='ios':
	sys.stdin=open('input1.txt')

def main():
	a,b = list(map(int, input().strip().split()))
	if 0 < a:
		print('Positive')
	else:
		if b >= 0:
			print('Zero')
		else:
			if (b-a) % 2 == 0:
				print('Negative')
			else:
				print('Positive')

main()
