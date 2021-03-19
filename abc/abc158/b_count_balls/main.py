#!/bin/python3

import sys
# input = sys.stdin.readline

if sys.platform =='ios':
	sys.stdin=open('input1.txt')

def main():
	n,a,b = list(map(int, input().strip().split()))
	result = n // (a+b) * a
	result += min(n % (a+b), a)
	print(result)
	
main()
