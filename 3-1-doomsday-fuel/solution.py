from fractions import Fraction
import fractions
import itertools
import math

def solution(m):
    t, r, ret = sum([1 for i in [ls for ls in m] if sum(i) != 0]), sum([1 for i in [ls for ls in m] if sum(i) == 0]), []
    # Step 3; Get R and Q submatrices
    r_subm, q_subm = split_matrix(m)

    # Step 4; Get identity submatrix
    iden_subm = make_id_m(len(q_subm))

    # Step 5; Inverse I - Q
    f_m = inverse(subtract_m(iden_subm, q_subm))

    # Step 6; Multiply F * R
    sol_m = convert_to_fractions(matmult(f_m, r_subm))
    
    # Find solution array
    sol_ar = sol_m[0]

    # Step 7; Find common denominator
    denum = find_denum(sol_ar)

    # Step 8; Find probabilities against each state
    for i in sol_ar:
        ret.append((i * denum).numerator)
    ret.append(denum)

    # Return all
    return ret

def convert_to_fractions(m):
    to_return = []
    for state in m:
        p_sum, temp = float(sum(state)), []
        for i in range(len(state)):
            if state[i] != 0:
                temp.append(Fraction(state[i]/p_sum).limit_denominator())
            else:
                temp.append(0)
        to_return.append(temp)
        del temp
    return (to_return)

def is_terminal(state):
    if sum(state) == 0:
        return True
    return False

def make_id_m(n):
    id = []
    for i in range(n):
        temp = []
        for j in range(n):
            if j == i:
                temp.append(1)
            else:
                temp.append(0)
        id.append(temp)
        del temp
    return (id)

def split_matrix(m):
    m = convert_to_fractions(m)
    absorbing = []
    for row_index in range(len(m)):
        if is_terminal(m[row_index]):
            absorbing.append(row_index)
    transient = [i for i in range(len(m)) if i not in absorbing]
    r_subm, q_subm = [], []
    for row_index in transient:
        rt, qt = [], []
        for col_index in range(len(m)):
            if col_index not in transient:
                rt.append(m[row_index][col_index])
            else:
                qt.append(m[row_index][col_index])
        r_subm.append(rt)
        q_subm.append(qt)
    return r_subm, q_subm

def subtract_m(m1, m2):
    # m1 should be larger than m2
    f = [[0 for i in range(len(m1))] for i in range(len(m1))]
    for r in range(len(m1)):
        for c in range(len(m1)):
            f[r][c] = m1[r][c] - m2[r][c]
    return f

def eliminate(r1, r2, col, target=0):
    fac = (r2[col]-target) / r1[col]
    for i in range(len(r2)):
        r2[i] -= fac * r1[i]

def gauss(a):
    # Helper to inverse matrix manually
    for i in range(len(a)):
        if a[i][i] == 0:
            for j in range(i+1, len(a)):
                if a[i][j] != 0:
                    a[i], a[j] = a[j], a[i]
                    break
            else:
                raise ValueError("Matrix is not invertible")
        for j in range(i+1, len(a)):
            eliminate(a[i], a[j], i)
    for i in range(len(a)-1, -1, -1):
        for j in range(i-1, -1, -1):
            eliminate(a[i], a[j], i)
    for i in range(len(a)):
        eliminate(a[i], a[i], i, target=1)
    return a

def inverse(a):
    tmp = [[] for _ in a]
    for i,row in enumerate(a):
        assert len(row) == len(a)
        tmp[i].extend(row + [0]*i + [1] + [0]*(len(a)-i-1))
    tmp = gauss(tmp)
    ret = []
    for i in range(len(tmp)):
        ret.append(tmp[i][len(tmp[i])//2:])
    return ret

def matmult(a, b):
    zip_b = zip(*b)
    # zip_b = list(zip_b)
    return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b)) 
             for col_b in zip_b] for row_a in a]

def lcm(a, b):
    # Beware! gcd is now implemented in `math` in Python 3+
    return abs(a*b) // fractions.gcd(a, b)

def find_denum(ar):
    x = 1
    k = itertools.combinations([x.denominator for x in ar],2)
    for item in k:
        res = reduce_fn(lcm, (a for a in item))
        if res > x:
            x = res
    return x
    
def reduce_fn(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value