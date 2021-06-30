#!/bin/python3

import sys
# input = sys.stdin.readline

if sys.platform =='ios':
	sys.stdin=open('input1.txt')

def main():
	n = list(map(int, input().strip().split()))[0]
	s = list(map(str, input().strip().split()))[0]
	
	if s[0]	!= s[-1]:
		print(1)
		sys.exit()
	for i in range(1, n-2):
		if s[0] != s[i] and s[i+1] != s[-1]:
			print(2)
			sys.exit()
	print(-1)

main()

