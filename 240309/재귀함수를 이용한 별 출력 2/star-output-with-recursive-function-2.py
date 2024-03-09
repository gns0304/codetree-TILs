def answer(n):
    if n == 0:
        return
    print('* ' * n)
    answer(n - 1)

def answer_1(n):
    if n == 0:
        return
    answer_1(n - 1)
    print('* ' * n)

n = int(input())
answer(n)
answer_1(n)