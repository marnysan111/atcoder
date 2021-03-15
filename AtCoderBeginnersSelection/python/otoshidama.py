

n, y  = map(int, input().split())
a = -1
b = -1
c = -1
for i in range(n+1):
    for j in range(n+1-i):
        m = n - i - j
        p = 10000*m + 5000*j + 1000*i

        if (y == p):
            a = m
            b = j
            c = i

print(a, b, c)

