def mergesort(a):
    n=len(a)-1
    mid=len(a)//2
    if n>1:
        return merge(mergesort(a[:mid+1]), mergesort(a[mid+1:]))
    else:
        return a
def merge(left, right):
    if len(left)==1:
        return right
    if len(right)==1:
        return left
    if left[0]<=right[0]:
        left.pop(0)
        a=merge(left, right)
        a.insert(0, left[0])
        return a
    else:
        right.pop(0)
        b=merge(left, right)
        b.insert(0, right[0])
        return b    
      
               
a=[10, 2, 5, 3, 7,13,1,6]
print(mergesort(a))