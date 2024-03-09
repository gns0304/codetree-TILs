def run_count(n):
    if n == 1:
        return 0
    
    if n % 2 == 0:
        return run_count(n // 2) + 1
    else:
        return run_count(n // 3) + 1

print(run_count(int(input())))