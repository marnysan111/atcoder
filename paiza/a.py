s = input()

ans = ""
d = {"a","i","u","e","o", "A", "I", "U", "E", "O"}


for i in s:
    if i in d:
        continue
    else:
        ans = ans + i

print(ans)