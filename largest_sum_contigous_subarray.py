def solve():
    n = int(input())
    l = [int(x) for x in input().split()]
    ans = l[0]
    for i in range(1, n):
        l[i] = max(l[i], l[i]+l[i-1])
        ans = max(ans, l[i])
    print(ans)    

for _ in range(int(input())):
    solve()
    
