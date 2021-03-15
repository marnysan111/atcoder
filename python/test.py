a = list(map(int, input().split()))

count = 0

for i in a:
    if i == 7:
        count += 1
    elif i==5:
        count += 1
    else:
        continue

if count == 3:
    print("YES")
else:
    print("NO")
