# a_n = a_(n-1) + a_(n-2)

def fibo(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(int(input())))