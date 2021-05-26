t = int(input())
for i in range(t):
    a, b, n = map(int,(input().split()))
    
    multiplier = n // 2
    if n % 2 != 0:
        a = a * 2
    if a > b:
        print(a // b)
    else:
        print(b // a)
