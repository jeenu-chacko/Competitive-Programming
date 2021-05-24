a=[input() for i in range(0,int(input()))]
b,c=[a[0]],[a.count(a[0])]
def sol(a):
    for i in a:
        if i not in b:
            b.append(i)
            c.append(a.count(i))
sol(a)
print(len(c))
print(*c)

