i = [input().split() for l in range(2)]

# ans = (a[0][0] * a[1][1]) - (a[0][1] * a[1][0])

a = int(i[0][0])
b = int(i[0][1])
c = int(i[1][0])
d = int(i[1][1])

ans = (a*d) - (b*c)
  
print(ans)
