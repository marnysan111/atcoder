N = int(input())
ans = 0
if 64 <= N:
    ans = 64
elif 32 <= N < 64:
    ans = 32
elif 16 <= N < 32:
    ans = 16
elif 8 <= N < 16:
    ans = 8
elif 4 <= N < 8:
    ans = 4
elif 2 <= N < 4:
    ans = 2
elif N == 1:
    ans = 1
print(ans)