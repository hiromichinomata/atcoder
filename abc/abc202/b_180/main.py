#!/bin/python3

import sys
# input = sys.stdin.readline

if sys.platform =='ios':
	sys.stdin=open('input1.txt')

def main():
	s = list(map(str, input().strip().split()))[0]
	result = ''
	for i in range(len(s)):
		t = s[i]
		if t == '6':
			t = '9'
		elif t == '9':
			t = '6'
		result += t
	print(result[::-1])

main()
