nx = input().split()

s1 = input()
s2 = [str(c) for c in s1]
p = int(nx[1])

for i in s2:
    if i == "o":
        p += 1
    elif i == "x":
        if p == 0:
            continue
        elif p > 0:
            p -= 1

print(p)

"""
for i in s2:
    if p == 0:
        break
    elif p > 0:
        if i == "o":
            p += 1
        elif i == "x":
            p -= 1

print(p)

"""

"""
for i in s2:
    if i == "o":
        print("oだお")
    elif i == "x":
        print("xだお")

"""