n=int(input())
#1000000000
l=list(range(1,44721))
i=0
t=lambda x:x*(x+1)/2
l1=[t(x)  for x in l if t(x)<=n]
final=n-l1[-1]
l=l[:len(l1)]
r=len(l1)
l[-1]=l[-1]+final
print(r)
for x in l:
    print(int(x),end=" ")


