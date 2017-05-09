from timeit import default_timer as timer
start = timer()
def prime_numbers(n):
    out = list()
    for x in range(1, n+1):
        if (x % i != 0 for i in range (2, int(x**.5)+1)):
            out.append(x)
    return out
end = timer()
print (end -start)
