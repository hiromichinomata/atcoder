#!/bin/python3

import sys
# input = sys.stdin.readline

if sys.platform =='darwin':
    sys.stdin=open('input1.txt')

def main():
    x, y = list(map(int, input().strip().split()))
    result = 0
    for i in range(x+1):
        if i * 2 +  (x-i)*4 == y:
            print('Yes')
            sys.exit()
            
    print('No')

main()
