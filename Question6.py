for i in range(int(input())):
    c,d,l=map(int, input().split())
    m=max(d,c-d)
    if m*4<=l<=(c+d)*4 and l%4==0:
        print("yes")
    else:
        print("no")
