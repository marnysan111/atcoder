def solution(A):
    N = len(A)
    count = [0]*(N + 1)
    
    # Counts all elements of A tha belongs to sequence {1, ..., N}
    for k in range(N):
        if N >= A[k] > 0:
            print(count)
            count[A[k]] += 1
        
    print(count)
    # Searches for the lesser integer that not belongs to A 
    for k in range(1, N + 1):
        if count[k] == 0:
            return k
    
    # If A has all elements from 1 to N, N + 1 is the minimal integer
    return N + 1



def main():
    a = input().split()
    b = [] * len(a)
    for i in range(len(a)):
        b.append(int(a[i]))
    
    c = solution(b)
    print(c)


if __name__ == "__main__":
    main()