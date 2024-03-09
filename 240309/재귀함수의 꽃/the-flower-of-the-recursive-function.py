def answer(n):
    if n == 0:
        return
    
    print(n, end = " ")
    answer(n-1)
    print(n, end = " ")

answer(int(input()))