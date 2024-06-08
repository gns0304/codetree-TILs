def answer(n):
    if n % 2 == 0:
        # 짝수
        if n <= 2:
            return 2
    else:
        # 홀수
        if n <= 1:
            return 1
    
    return answer(n-2) + n
    
print(answer(int(input())))