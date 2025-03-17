N=int(input("enter the number of rows for which you want *"))
for i in range(N):
    for j in range(N-i):
        print("*",end="")
    print("")

