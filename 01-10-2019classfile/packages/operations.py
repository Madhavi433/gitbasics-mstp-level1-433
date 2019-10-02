def add(a,b):
    m=a+b
    print(m)
    
def prime(i):
    fact=0
    for j in range(1,i+1):
        if i%j==0:
            fact=fact+1
    if fact==2:
         print("true")
    else:
         print("false")
             
def prime_factors(n):
        for i in range(1,n+1):
            if n%i==0:
                print(i,end=" ")