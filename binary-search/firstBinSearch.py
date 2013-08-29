## binary search implementation in python

def binarysearch(searchSet, key):
	lo, hi = 0, len(searchSet)
	mid = (hi - lo) // 2 ## note that integer division gives the same result for implementations in both python3 and python2
	while lo <= hi:
		if searchSet[mid] == key:
			return mid
		else if searchSet[mid] > key:
			hi = mid
			mid = (hi - lo) // 2
		else 
			lo = mid
			mid = (hi - lo) // 2
	return -1

