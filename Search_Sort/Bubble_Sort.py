arr= [12,5,8,4,9,6,3,7,18,1,3]
n= len(arr)

pas=1

while(pas<=n-1):
    index=0
    while index<=n-pas-1:
        if arr[index]>arr[index+1]:
            arr[index],arr[index+1]=arr[index+1],arr[index]
        index = index+1
    pas=pas+1

for i in arr:
    print (i)