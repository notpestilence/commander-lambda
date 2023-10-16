def solution(l):
    c, trips = [0] * len(l), 0
    for i in range(len(l)):
        for j in range(i):
            if (l[i] % l[j] == 0):
                c[i] += 1 # the number of previous integers that divides l[i]
                trips += c[j] # the number of previous integers that divides l[j]
    return trips