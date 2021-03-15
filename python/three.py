def main():
    a, b = map(int, input().split())
    if a > b:
        b += 3
        if b > a:
            print("Yes")
        else:
            print("No")
    else:
        a += 3
        if a > b:
            print("Yes")
        else:
            print("No")
                



if __name__ == "__main__":
    main()