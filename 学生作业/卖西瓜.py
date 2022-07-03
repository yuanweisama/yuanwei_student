n = int(input('输入西瓜总个数'))
a = 0
while n >1:
    n=n-n/2-1
    a+=1
print(a)