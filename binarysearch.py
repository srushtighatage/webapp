def binarysearch(array,key,start,end):
    if start<=end:
        mid=start+(end-start)//2
        if array[mid]==key:
            return mid
        elif array[mid] >key:
            return binarysearch(array,key,start,mid-1)
        else:
            return binarysearch(array,key,mid+1,end)
array=[3,4,5,6,7,8,9]
key=10
result=binarysearch(array,key,0,len(array)-1)
if result != -1:
    print("eliment is present at position ==>" +str(result))
else:
    print("oops eliment is not present")