a=[5,8,3,1,7,9,4,6]
print(a)

x=int(input("enter number to search"))

i=flag=0


while i<len(a):
    if a[i] == x:
        flag =1
        break
    i=i+1
if flag ==1:
    print(i+1)
else:
    print("not found")