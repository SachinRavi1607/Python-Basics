def countzeroes(n):
    
    if(n%10==n):
        print(n)
        if n%10==0:
            return 1
        else:
            return 0

    if n%10==0:
        return 1+countzeroes(n//10)
    else:
        return countzeroes(n//10)
    

    # Test the function with n = 1000
X=countzeroes(1000)
print("Number of zeros in 1000: ",X)