for _ in range(int(input())):
    flag=0
    n=int(input())
    s=input().split()
    for i in range(0,n):
        if s[i]=="cookie" and (i+1==n or s[i+1]!='milk'):
            flag=1
            break
    if flag==0:
        print("YES")
    else:
        print("NO")
