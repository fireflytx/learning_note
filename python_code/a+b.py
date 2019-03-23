import random
y = int(input("请输入随机最大数："))
x = int(input("请输入算数题数量："))
k = 4
g = len(str(y))
fa =f"{{:{g}}}"

i = 0
for i in range(1+(x//k)):
    if i < x//k :
        z = k

    else :
        z = x % k

    for j in range (z):
        a = random.randint(0,y)
        b = random.randint(0,y)
        c = random.choice(["+", "-"])
    
        print(fa.format(a),c,fa.format(b),'=      ',end=' ')

    print()
    
