# Binary Search

## 1. Search

Template Code:

```
def bsearch(array, l, r, target):
	while l <= r:
		mid = 1 + (r-1) / 2
		if array[mid] > target:
			r = mid - 1
		elif array[mid] < target:
			l = mid
		else:
			return mid
	return -1
```

## 2. >=

## 3. <=

## 4. Range

## 5. Sorted Array

## 6. Two Halves
