# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    else:
    	print("start")
    	print(a[left:right])
    	(ml, mr) = (majority(a[left:right], get_majority_element(a, 0, int((right-1)/2))), majority(a[left:right+1], get_majority_element(a, int(right/2), right-1)))
    	print("*")
    	print(a[left:right])
    	if ml != -1:
    		return ml
    	if mr != -1:
    		return mr
    return -1
def majority(current_array,key):
  	count = 0
  	for i in current_array:
  		if key == i:
  			count += 1
  			if count > len(current_array)/2:
  				return key
  	return -1
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
