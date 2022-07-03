N=int(input('输入整数'))
sum=0
for i in range(1,N):
    if i%2==0:
        i=i**2
        sum+=i
print(sum)

