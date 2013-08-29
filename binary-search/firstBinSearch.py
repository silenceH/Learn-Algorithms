## binary search implementation in python

def binarysearch(searchSet, key):
	lo, hi = 0, len(searchSet)
	
	while lo < hi:
		mid = (lo + hi) // 2 ## note integer division
		midval = searchSet[mid]
		if midval < key:
			lo = mid + 1
		elif midval > key:
			hi = mid
		else: 
			return mid
	return -1

