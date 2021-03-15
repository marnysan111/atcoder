i = list(map(int,input().split()))
n = i[0]
t = int(i[1])

a = list(map(int,input().split()))

ans = 0

for j in a:
    if j < t:
        if ans < t:
            print("if",j)
            ans += j
        elif ans > t:
            print("elif",j)
            pass
    elif j > t:
        pass

print(ans)



