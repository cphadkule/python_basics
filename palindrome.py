a = "aba"
a= list(a)
b= list.copy(a)
b.reverse()

if a==b:
    print("YES")
else:
    print("NO")