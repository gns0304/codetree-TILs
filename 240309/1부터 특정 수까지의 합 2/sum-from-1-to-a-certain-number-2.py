def answer(n):
    if n == 0:
        return 0
    return answer(n-1) + n

print(answer(int(input())))