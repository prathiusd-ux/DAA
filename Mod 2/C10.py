def karatsuba(x, y):
    if x<10 or y<10:
        return x*y

    lenx=len(str(x))
    leny=len(str(y))
    n=max(lenx, leny)
    m=n//2

    A=x//10**m
    B=x%10**m
    C=y//10**m
    D=y%10**m

    AC=karatsuba(A,C)
    BD=karatsuba(B,D)
    ADplusBC=karatsuba(A+B, C+D)-AC-BD

    return AC*10**(2*m) + ADplusBC*10**m +BD


n1=int(input("enter the first number:"))
n2=int(input("enter the second number:"))
print(karatsuba(n1, n2))