from bisect import bisect_right, bisect_left
n,x = map(int, input().split())

lst = list(map(int, input().split()))

a = bisect_left(lst, x)
b = bisect_right(lst, x)

if b-a == 0:
    print(-1)
else:
    print(b-a)