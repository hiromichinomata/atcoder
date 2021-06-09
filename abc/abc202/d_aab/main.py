#!/bin/python3

import sys
# input = sys.stdin.readline

if sys.platform =='ios':
	sys.stdin=open('input1.txt')

from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

def main():
	a, b, k = list(map(int, input().strip().split()))
	result = ''
	while k > 0 and a > 0 and b > 0:
		num = cmb(a-1+b,a-1)
		if num >= k:
			result += 'a'
			a -= 1
		else:
			result += 'b'
			k -= num
			b -= 1
	if a == 0:
		result += 'b'*b
	if b == 0:
		result += 'a'*a
	print(result)

main()
