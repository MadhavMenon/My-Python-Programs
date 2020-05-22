n=int(input())
m=[]
for i in range(n):
    a=input().split(' ')
    a=[int(x) for x in a]
    m.append(a)
print(m)
m1=sorted(m, key=lambda x: x[0])
count=0
check=m1[0][1]
i=0
c=[]
while True:
    u=0
    for j in range(i+1,len(m1)):
        if check in list(range(m1[j][0],m1[j][1]+1)):
            u=1
        else:
            check=m1[j][1]
            c1=m[j][1]
            break
    if(u==1):
        count+=1
        c.append(c1)
        

            
print(count)    
for x in c:
    print(x,end=" ")
