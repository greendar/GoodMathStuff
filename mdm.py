def fact(n):
    prod = 1
    if n == 0:
        return 1
    for i in range(n):
        prod = prod * (i + 1)

    return prod

def perm(n, r):
    return int(fact(n)/fact(n-r))

def comb(n, r):
    return int(fact(n)/(fact(r)*fact(n-r)))

def pascal(n):
    for i in range(n+1):
        for j in range(i+1):
            print(comb(i, j), end=" ")
        print()


print(pascal(15))