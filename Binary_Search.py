def bsearch(arr,start,last,element):

    mid=int((start+last)/2)
    if start>last:
        print("element not found")
    elif element < arr[mid]:
        last = mid-1
        bsearch(arr,start,last,element)
    elif element > arr[mid]:
        start = mid+1
        bsearch(arr, start, last, element)
    else:
        print(str(mid+1))


arr=[1,3,5,7,9,11,13,15,17,19]
element = 1
start = 0
last = len(arr)-1
bsearch(arr,start,last,element)
