def maxValue(arr):
    for i in range(0,len(arr)-1):
        if arr[i]<arr[i+1]:
            continue
        else:
            arr[i],arr[i+1]=arr[i+1],arr[i]

    return arr
n=int(input())
arr=[]
for i in range(0,n):
    a=int(input())
    arr.append(a)
print(maxValue(arr))
