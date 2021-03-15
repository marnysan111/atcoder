h, w = map(int, input().split())

c =  [input().split() for l in range(h)]

l = [["B" for i in range(w)] for j in range(h)]

for i in range(h):
    score = 0
    judge = 0
    for j in range(w):
        score += int(c[i][j])
    for j in range(w):
        judge += int(c[i][j])
        if judge == (score/2):
            ans = "Yes"
            for m in range(j+1):
                l[i][m] = "A"
            break
        else:
            ans = "No"

if ans == "Yes":
    print("Yes")
    print(*l)
else:
    print("No")



h, w = map(int, input().split())

c =  [input().split() for l in range(h)]

l = [["B" for i in range(w)] for j in range(h)]

for i in range(h):
    score = 0
    judge = 0
    for j in range(w):
        score += int(c[i][j])
    for j in range(w):
        judge += int(c[i][j])
        if judge == (score/2):
            ans = "Yes"
            for m in range(j+1):
                l[i][m] = "A"
            break
        else:
            ans = "No"

if ans == "Yes":
    print("Yes")
    for inner in l:
	    print(''.join(inner))
        
else:
    print("No")