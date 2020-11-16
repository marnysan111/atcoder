

n = int(input())

a = list(map(int,input().split()))

count = 0
loop = [0]
for i in loop[:]:
    for b in a:
        if (b % 2) == 0:
            None
        else:
            print("だめー")
            break
    for b in a:
        a[count] = b // 2
        count = count + 1
    count = 0
    loop.append(i+1)

print(a)