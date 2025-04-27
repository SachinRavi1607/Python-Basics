def sum_numbers(n):
    if n==0:
        return 0
    return (n%10)+sum_numbers(n//10)
X=sum_numbers(34534)

print(X)
