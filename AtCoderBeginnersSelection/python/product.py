a = list(map(int,input().split()))

b = a[0] * a[1]

def num(b):
    if (b % 2) == 0:
        print("Even")
    else:
        print("Odd")


num(b)