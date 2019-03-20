import random
y = int(input("请输入随机最大数："))
x = int(input("请输入算数题数量："))
k = 4
i = 0
for i in range(1+(x//k)):
    if i < x//k :
        z = k+1

    else :
        z = x % k + 1

    for j in range (z-1):
        a = random.randint(10,y)
        b = random.randint(10,y)
        c = random.choice(["+", "-"])
    
        print(a,c,b,'=   ',end=' ')

    print()
