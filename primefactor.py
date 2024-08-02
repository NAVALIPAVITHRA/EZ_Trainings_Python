def prime_factor(num):
    i=2
    factors={}
    while i*i<=num:
        while (num%i)==0:
            if i in factors:
                factors[i]=factors[i]+1
            else:
                factors[i]=1
        i+=1
    if num>1:
        factors[num]=1
    return factors