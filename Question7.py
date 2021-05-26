t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    s=list(set(l))
    stack=[]
    for i in s:
        if(l.count(i)>1):
            if(l.count(i)<4):
              stack.append(i)
            else:
              stack.append(i)
              stack.append(i)
    if(len(stack)>1):
        stack.sort()
        print(stack[len(stack)-1]*stack[len(stack)-2])
    else:
        print(-1)
