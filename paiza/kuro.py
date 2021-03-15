s = input()

s1 = s.replace('-', '')

ans = 0

for i in list(s1):
    if i == "0":
        ans += 24
    else:
        ans += int(i)*2 +4

print(ans)
    

