import sys
import random
def function1(arr):
    max1 = arr[0]
    for i in arr:
        if i>max1:
            max1=i
    arr.remove(max1)    
    max2=arr[0]
    for i in arr:
        if i>max2:
            max2=i
    return(int(max1)*int(max2))                     




if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(function1(input_numbers))
