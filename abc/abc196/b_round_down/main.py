#!/bin/python3

import sys
# input = sys.stdin.readline

if sys.platform =='ios':
	sys.stdin=open('input1.txt')

def main():
	s = list(map(str, input().strip().split()))[0]
	result = s.split('.')
	print(result[0])

main()
