def stars(n):
    if n == 0:
        return
    stars(n-1)
    print('*' * n)

stars(int(input()))