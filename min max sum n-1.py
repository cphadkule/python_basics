totnum =int(input())
num = list(map(int,input().split()))


total=0

for i in num:
    total =total + i

minimum = total - max(num)
maximum= total - min(num)

print(minimum, maximum)
