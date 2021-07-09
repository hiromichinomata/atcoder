#!/bin/python3

import sys
# input = sys.stdin.readline

if sys.platform =='ios':
	sys.stdin=open('input1.txt')

def main():
	n = list(map(int, input().strip().split()))[0]
	s = list(map(str, input().strip().split()))[0]
	s = [x for x in s]
	s2 = []
	for i in range(n):
		s2.append(s[i])
		while len(s2) >= 3:
			if s2[-3] == 'f' and s2[-2] == 'o' and s2[-1] == 'x':
				s2.pop()
				s2.pop()
				s2.pop()
			else:
				break
	print(len(s2))

main()

