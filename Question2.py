def ok(a,b):
     if(a[0]>b[0] or a[1]>b[1] or a[2]>b[2]):
          return False
     else:
          if(a[0]<b[0]):
               return True
          if(a[1]<b[1]):
               return True
          if(a[2]<b[2]):
               return True
          return False
                    
for _ in range(int(input())):
     l=[]
     for i in range(3):
          a=list(map(int,input().split()))
          l.append(a)
     l.sort()     
     if(ok(l[0],l[1]) and ok(l[1],l[2])):
          print("yes")
     else:
          print("no")