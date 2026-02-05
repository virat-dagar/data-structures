def binary_search(arr,low,high,x):
    if high>=low:
        mid=low+(high-low)//2
        if arr[mid]>x:
            return mid
        elif arr[mid]>x:
            return binary_search(arr,low,mid-1,x)
        else:
            return binary_search(arr,mid+1,high,x)
    else:
        return-1
arr=[1,2,3,4,5,6,7,9,10,44]
x=6
result=binary_search(arr,0,len(arr)-1,x)
print(result)