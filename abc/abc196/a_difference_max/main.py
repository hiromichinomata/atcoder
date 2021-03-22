#!/bin/python3

import sys
# input = sys.stdin.readline

if sys.platform =='ios':
	sys.stdin=open('input1.txt')

def main():
	a,b = list(map(int, input().strip().split()))
	c,d = list(map(int, input().strip().split()))
	print(b-c)

main()
