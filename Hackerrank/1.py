if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
if (2<=n<=10 and (-100<=a<=100 for a in arr)):
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
if (2<=n<=10 and (-100<=a<=100 for a in arr)):
    for i in range(n-1,-1,-1):
        for j in range(n-2,-1,-1):
            if arr[i]>arr[j]:
                print(arr[j])
                break
        break
              