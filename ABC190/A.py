a, b, c = map(int, input().split())

if c == 0:
    if a > b:
        print("Takahashi")
    elif a == b:
        print("Aoki")
    else:
        print("Aoki")

if c == 1:
    if a < b:
        print("Aoki")
    elif a == b:
        print("Takahashi")
    else:
        print("Takahashi")