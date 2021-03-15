n = int(input())

count = -1

for i in range(n+1):
    if len(str(i)) % 2 == 1:
        count += 1


print(count)