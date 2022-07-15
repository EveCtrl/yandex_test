def Factor(n):
    Ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            Ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        Ans.append(n)
    return Ans

from math import gcd

n = int(input())
while n > 0:
    n = n - 1
    a, b = input().split()
    a, b = int(a), int(b)
    d_a, d_b = Factor(int(a)), Factor(int(b)) # делители
    cd = list(set(d_a).union(d_b)) # общие делители
    cd.sort()
    for elem in cd[::-1]:
        if d_a.count(elem) > d_b.count(elem):
            b *= elem
            break
        if d_b.count(elem) > d_a.count(elem):
            a *= elem
            break
    print(gcd(a, b))