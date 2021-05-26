t=int(input())
for i in range(t):
	n=int(input())
	a=list(map(int,input().split()))
	a.sort()
	print(a[0]*(len(a)-1))
