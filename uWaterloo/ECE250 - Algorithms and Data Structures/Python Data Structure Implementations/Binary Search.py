def findNumber(arr,k):
    arr.sort()
    print arr
    if arr == []: return "NO"
    mid = (int) (len(arr)//2)
    if k == arr[mid]:
      return "YES"
    elif k > arr[mid]:
        return findNumber(arr[mid+1:len(arr)],k)
    elif k <= arr[mid]:
        return findNumber(arr[0:mid-1],k)
    else:
        return "NO"
        
print findNumber([8,7,6,5,4,3,2,1],8)
