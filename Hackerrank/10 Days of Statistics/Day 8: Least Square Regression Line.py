n = 5
xy = [map(int, input().split()) for _ in range(n)]
sx, sy, sx2, sxy = map(sum, zip(*[(x, y, x**2, x * y) for x, y in xy]))
b = (n * sxy - sx * sy) / (n * sx2 - sx**2)
a = (sy / n) - b * (sx / n)
X=80
ans=a+b*X
print(round(ans,3))