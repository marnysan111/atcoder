num = lambda c: ord(c) - ord('a') + 1



s = input()
s = s.replace(' ', '')
ans = []
count = 0
for i in s:
    ans.append(i)
print(s)