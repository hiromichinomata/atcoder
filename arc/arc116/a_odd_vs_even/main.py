#!/bin/python3

import sys
# input = sys.stdin.readline
import math

if sys.platform =='ios':
	sys.stdin=open('input1.txt')

def main():
	t = list(map(int, input().strip().split()))[0]
	for i in range(t):
		n = list(map(int, input().strip().split()))[0]
		if n % 4 == 0:
			print('Even')
		elif n % 2 == 0:
			print('Same')
		else:
			print('Odd')

main()
