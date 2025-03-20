N=int(input("enter the number of rows for which you want to print the inverted pattern:"))
for i in range(1,N+1):
    for j in range(i-1):
        print(" ",end="")
    for j in range(2*N-((2*i)-1)):
        print("*",end="")

    print()