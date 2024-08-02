
n = int(input())
arr = list(map(int, input().split()))
m = int(input())
c = 0  # Initialize counter

for r in range(n-2):
    i, j = r+1, n-1  # Initialize j to n-1
    while i < j:
        pro = arr[i] * arr[j] * arr[r]
        if pro > m:
            j -= 1  # Decrement j
        elif pro < m:
            i += 1
        else:
            i += 1
            j -= 1
            c += 1

print(c)
