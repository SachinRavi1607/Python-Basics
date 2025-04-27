
def coutnumbers(n):
    if n==0:
        return 0

    return 1+coutnumbers(n//10)
X=coutnumbers(353445)
print(X)