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

**1. Two Sum II - Input Array is Sorted**

**2. Search a 2D Matrix**

**3. H-Index II**

**4. Search a 2D Matrix II**

**5. Find Peak Element**

## 2. >=

## 3. <=

## 4. Range

## 5. Sorted Array

## 6. Two Halves
