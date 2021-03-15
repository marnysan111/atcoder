n, s, d = map(int, input().split())

xy = [input().split() for l in range(n)]

count = 0

for i in xy:
    if int(i[0]) < s:
        if int(i[1]) > d:
            #print("Yes")
            count += 1
        else:
            #print("No")
            continue
    else:
        #print("No")
        continue

if count >= 1:
    print("Yes")
else:
    print("No")
