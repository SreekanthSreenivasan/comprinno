t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    a = lst.count(0)
    b = lst.count(1)
    c = lst.count(-1)
    d = n - (a+b+c)
    
    if(d>1 or (c>0 and d>0) or (c>1 and b==0)):
        print('no')
    else:
        print('yes')
