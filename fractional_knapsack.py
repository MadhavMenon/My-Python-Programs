n1=input().split(' ')
n=int(n1[0])
W=int(n1[1])
knapsack=[]
for i in range(n):
    l=[]
    a=input().split(' ')
    l.append(int(a[0]))
    l.append(int(a[1]))
    l.append(int(a[0])/int(a[1]))
    knapsack.append(l)
knapsack=sorted(knapsack,key= lambda x:x[2],reverse = True)
   
w=W
i=0
cost=float(0)
while(w!=0):
    if(i>=len(knapsack)):
        
        break
    if(w<knapsack[i][1]):
        cost+=(knapsack[i][2]*w)*1000/1000
    elif(w>=knapsack[i][1]):
        w-=(knapsack[i][1])
        cost+=knapsack[i][0]
        
    i+=1    
    
print(round(float(cost), 4))          
