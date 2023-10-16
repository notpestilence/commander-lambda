def to_bin(n):
    n = int(n)
    return(bin(n)[2:])

def solution(n):
    n = int(n)
    count = 0
    while n > 3:
        if int(to_bin(n)) % 2 == 0:
            n /= 2
        elif to_bin(n)[-3:] == "001":
            n -= 1
        elif to_bin(n)[-3:] == "111":
            n += 1
        elif to_bin(n)[-3:] == "101":
            n -= 1
        elif to_bin(n)[-3:] == "011":
            n += 1
        count += 1
    if n == 3:
        count += 2
        return count
    elif n == 2:
        count += 1
        return count
    elif n == 1:
        return count
