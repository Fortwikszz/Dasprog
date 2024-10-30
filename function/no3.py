n = int(input())

def fibo(n, N, min1, min2):
    if n == 1:
        return "0"
    elif N == 0:
        return ""
    elif N == n:
        return (f"0{fibo(n, N-1, min1=0, min2=0)}")
    elif N == n-1:
        return (f",1{fibo(n, N-1, min1=1, min2=0)}")
    else:
        return (f",{min1+min2}{fibo(n, N-1, min1=(min1+min2), min2=min1)}")  
    
print(fibo(n,n,0,0))