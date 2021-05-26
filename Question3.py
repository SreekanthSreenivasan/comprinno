for _ in range(int(input())):
    s = int(input())
    n = list(map(int, input().split()))
    N = len(n)
    mid = N // 2 + 1
    if N % 2 == 0:
        print("no")
    else:
        flag = "yes"
        if n[0] == 1:
            for i in range(0, mid - 1):
                for j in range(mid - 1, N - 1):
                    if n[j] - n[j + 1] == 1 and n[i + 1] - n[i] == 1:
                        pass
                    else:
                        flag = "no"
                        break
                break
            print(flag)
        else:
            print("no")