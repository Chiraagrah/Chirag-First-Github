def gcd(m,n):
    if m<n:
        m,n = n,m
    if m%n==0:
        return n
    else:
        gcd(n,m%n)
a=input("Enter The First Number: ")
b=input("Enter The Second Number: ")        
print("GCD of ",a," ,",b," is ",gcd(a,b))