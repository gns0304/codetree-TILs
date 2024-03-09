def answer_descending(N):
    if N == 0:
        return
    print(N, end=" ")
    answer_descending(N-1)

def answer_ascending(N):
    if N == 0:
        return
    answer_ascending(N-1)
    print(N, end = " ")
    
N = int(input())
answer_ascending(N)
print()
answer_descending(N)