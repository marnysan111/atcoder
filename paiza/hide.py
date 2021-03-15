import sys

a = list(map(int,input().split()))

b = [[str(c) for c in l.strip()] for l in sys.stdin]


ans = ""
jud = 0


for i in range(a[0]):
    for j in range(a[2]):
        ans += b[i][j]
    if jud < int(ans):
        jud = int(ans)
    print(ans)
    ans=""
    for j in range(a[2]):
        ans += b[i][j+1]
    print(ans)
    ans=""
print(jud)
print("-----")
for i in range(a[0]):
    for j in range(a[2]):
        ans += b[j][i]
    if jud < int(ans):
        jud = int(ans)
    print(ans)
    ans = ""
    for j in range(a[2]):
        ans += b[j+1][i]
    if jud < int(ans):
        jud = int(ans)
    print(ans)
    ans = ""
print(jud)


"""
jud = 0

for i in range(a[0]):
    for j in range(a[0]-1):
        tmp = (b[i][j] * 10) +  (b[i][j+1])
        if jud < tmp:
            jud = tmp 

for i in range(a[0]):
    for j in range(a[0]):
        tmp = (b[i][j] * 10) + (b[i+1][j])
        print(j)
        if jud < tmp:
            jud = tmp 
print(jud)

"""