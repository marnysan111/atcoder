h, w = map(int, input().split())

s = [str(input()) for l in range(h)]

p = [input().split() for l in range(h)]

score = 0

for i in range(h):
    for j in range(w):
        if s[i][j] == "o":
            score += p[i][j]

print(score)