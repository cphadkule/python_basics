arr= [12,5,8,4,9,6,3,7,18,1,3]
min =0
n=len(arr)

while min<=n-1:
    next=min
    while next<=n-1:
        if arr[next] < arr[min]:
            arr[next],arr[min] = arr[min],arr[next]
        next = next+1
    min = min +1

for i in arr:
    print (i)