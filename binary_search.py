arr=input().split(' ')
arr=[int(x) for x in arr]
arr=arr[1:]
arr.sort()
a=input().split(' ')
a=[int(x) for x in a]
a=a[1:]
def Binary(arr, l, r, x): 
  
    while l <= r: 
  
        mid = l + (r - l)//2; 
          
        # Check if x is present at mid 
        if arr[mid] == x: 
            return mid 
  
        # If x is greater, ignore left half 
        elif arr[mid] < x: 
            l = mid + 1
  
        # If x is smaller, ignore right half 
        else: 
            r = mid - 1
      
    # If we reach here, then the element was not present 
    return -1
l=[]   
y=len(arr)-1
for i in a:
    l.append(Binary(arr,0,y,i))
for i in l:
    print(i," ",end=" ")    