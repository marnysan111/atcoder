import sys

h, w, k = map(int, input().split())

s = [[str(c) for c in l.strip()] for l in sys.stdin]

test1 = ""
test2 = ""
test3 = ""

Max = 0


for i in range(h):
    for j in range(k):
        for n in range(k):
            test1 += s[i][n]
    print(test1)
    test1 = ""



"""
# 横で判断する
for i in range(h):
    for j in range(k):
        test1 += s[i][j]
        test2 += s[i][j+1]
        test3 += s[i][j+2]
    print(test1, test2, test3)
    if Max < test1:
        Max 
    test1 = ""
    test2 = ""
    test3 = ""
"""