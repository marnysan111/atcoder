m, n, k = map(int, input().split())

a = [input().split() for l in range(k)]

a1 = []

for i in range(k):
    a1.append(0)


for i in a:
    q = 0
    print(i)
    q = a1[i]
    print(q)

print(a1)
