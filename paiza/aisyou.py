num = lambda c: ord(c) - ord('a') + 1
s = input()
s = s.replace(' ', '')
count = 0
ans = []
for i in s:
    ans.append(num(i))

a = list()
while True:
    if count == int(len(ans) - 1):
        ans = a
        count = 0
        a = list()
        if len(ans) == 1:
            break
        else:
            continue
    else:
        x = ans[count] + ans[count+1]
        if x >= 101:
            x -= 101
            a.append(x)
        else:
            a.append(x)
        count += 1

print(*ans)