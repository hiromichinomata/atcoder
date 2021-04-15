#!/bin/python3

import sys
# input = sys.stdin.readline

if sys.platform =='ios':
	sys.stdin=open('input1.txt')

def main():
	n = list(map(str, input().strip().split()))[0]

	for i in range(10):
		s = '0' * i + n
		if s == s[::-1]:
			print('Yes')
			sys.exit()
			
	print('No')
	
main()
