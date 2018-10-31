num = [1,2,3,4,5]



total=0

for i in num:
    total =total + i

min = total - max(num)
max= total -min(num)

print(min, sep="")
print(max)