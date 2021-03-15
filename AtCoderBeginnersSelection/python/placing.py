a = input()

b = [int(c) for c in a]

count = 0

for d in b:
    if d == 1:
        count = count + 1
    else:
        pass

print(count)