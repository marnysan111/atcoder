

n = int(input())

a = list(map(int,input().split()))

loop = 0
count = -1
while loop < 1:
    for i in range(n):
        if a[i] % 2 == 1:
            loop += 2
        elif a[i] % 2 == 0:
            a[i] = a[i] / 2
    count += 1

print(count)