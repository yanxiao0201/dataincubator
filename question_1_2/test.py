def matrix(n):
    total = 0
    for i in xrange(1,n+1):
        for j in xrange(1,n+1):
            total = total + abs(i-j)

    for i in xrange(1,n+1):
        total += i

    return float(total)/n


def run(n):
    for i in xrange(1,n+1):
        print matrix(i)
