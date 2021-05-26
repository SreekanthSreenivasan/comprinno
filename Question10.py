t=int(input())
for i in range(t):
    sal=int(input())
    if(sal<1500):
        hra=10*sal/100
        dr=90*sal/100
        gross=sal+hra+dr
        print(gross)
    else:
        hra=500
        dr=98*sal/100
        gross=sal+hra+dr
        print(gross)
