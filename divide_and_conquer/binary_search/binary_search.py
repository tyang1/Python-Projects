# Uses python3
import sys
import math
from copy import deepcopy

def binary_search(a, x):
    left, right = 0, len(a)
    if right == 1 and a[0] != x:
    	#print (-1)
    	return -1
    mid =int((right-left)/2)
    if right == 2 and a[mid] != x:
    	#print(-1)
    	return -1
    #print (str(mid) + " " + str(a[mid]) + "the value to compared is x " + str(x))
    if a[mid] == x:
    	#print (mid)
    	return mid
    if a[mid] > x:
    	return binary_search(a[0:mid-1], x)
    else:
    	return binary_search(a[mid+1:], x)

    # write your code here

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
    	#binary_search(a,x)
    	print(binary_search(a, x), end = ' ')
        # replace with the call to binary_search when implemented
        #print(linear_search(a, x), end = ' ')
