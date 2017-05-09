from timeit import default_timer as timer
start = timer()
def prime_numbers(n):
    out = list()
    for x in range(1, n+1):
        prime = True
        for i in range(2, x):
            if (x % i == 0):
                prime = False
        if prime:
            out.append(x)
    return out
end = timer()
print (end -start)
