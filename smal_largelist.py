#n=int(input("enter no of elements:"))
arr=list(map(int,input().split()))
def small_and_large():
    smallest=arr[0]
    largest=arr[0]  
    for i in range(len(arr)):
        if arr[i]<smallest :
            smallest=arr[i]
        if arr[i]>largest:
            largest=arr[i]
    return smallest,largest
        
def main():
    print(small_and_large()) 
main()