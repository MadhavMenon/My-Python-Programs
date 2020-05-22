n=int(input())
a=input().split(' ')
a=[int(x) for x in a]
b=input().split(' ')
b=[int(x) for x in b]
a.sort()
b.sort()

def dot(x, y):
    return sum(m*n for m,n in zip(x,y))
print(dot(a, b))    