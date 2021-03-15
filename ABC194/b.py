n = int(input())

ab = [input().split() for i in range(n)]
min_a = []
min_b = []
min_a.append(ab[0][0])
min_b[0] = ab[1][0]

for i in range(n):
    if min_a > ab[i][0]:
        min_a[0] = ab[i][0]
        min_a[1] = i
    if min_b > ab[i][1]:
        min_b[0] = ab[i][1]
        min_b[1] = i

print(min_a)

print(min_b)

