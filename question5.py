t = int(input())
    
for q in range(t):
    
    n = int(input())
    a = list(map(int,input().split()))
    
    greater_than_one = 0
    one = 0
    zero = 0
    minus_one = 0
    negative = 0
    
    flag = 0
    for i in range(len(a)):
        if a[i] > 1:
            greater_than_one += 1
        elif a[i] == 1:
            one += 1 
        elif a[i] == 0:
            zero += 1 
        elif a[i] < 0:
            negative += 1
            if a[i] == -1:
                minus_one += 1
        
    
    
    if greater_than_one >= 2:
        flag = 1 
        
    elif greater_than_one >0 and negative >0:
        flag = 1 
        
        
    elif negative >= 2:
        if negative != minus_one:
            flag = 1 
            
        elif one == 0:
            flag = 1 
   
        
    if flag == 0:
        print("yes")
    else:
        print("no")
