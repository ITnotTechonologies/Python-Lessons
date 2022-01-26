n, m = map(int, input().split())


# arr = [[0]*n]*n
# print(arr)

res = [0]*n

for i in range(m):
    a, b = map(int, input().split())
    res[a - 1] += 1
    res[b - 1] += 1

for i in range(n):
    # res[i] //= 2
    print(res[i], end = ' ')
