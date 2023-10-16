def to_base_n(int_base_10, n):
    """
    Converts base 10 number to base n. Arguments:

    `int_base_10`: Integer input in base 10.\n
    `n`: Target base.

    Returns `int_base_10` reduced to base `n`.
    """
    residual = int(int_base_10)
    digits_base_n = []
    while residual >= n:
        r = residual % n
        digits_base_n.append(str(r))
        residual = (residual - r) // n
    digits_base_n.append(str(residual))
    return ''.join(digits_base_n[::-1])

def from_base_n(int_base_n, n):
    """
    Converts base n number to base 10. Arguments:

    `int_base_n`: Integer input in base `n`.\n
    `n`: Base number of `int_base_n`.

    Returns `int_base_n` converted to base 10.
    """
    x = list(int_base_n[::-1])
    y_base_10 = 0
    for i, a in enumerate(x):
        y_base_10 += int(a) * (n ** i)
    return str(y_base_10)

def solution(n, b):
    k = len(n)
    m = n
    mini_id = [] # Save seen Minion IDs

    # Check whether the current Minion ID is already seen
    while m not in mini_id:
        # Save current Minion ID 
        mini_id.append(m)
        s = sorted(m)
        x_descend = ''.join(s[::-1])
        y_ascend = ''.join(s)        
        # Check whether base is 10
        if b == 10:
            # Continue as instructed...
            int_m = int(x_descend) - int(y_ascend)
            m = str(int_m)
        else:
            int_m_10 = int(from_base_n(x_descend, b)) - int(from_base_n(y_ascend, b)) # Calculate `m` in Base 10
            m = to_base_n(str(int_m_10), b) # Cast `m` to base `b`
        # Pad with zeroes
        m =  (k - len(m)) * '0' + m
    
    # If `m` is seen, while loop will break
    # Get the index of which `m` was first seen
    # Subtract from the current length of `mini_id`. Return.
    return len(mini_id) - mini_id.index(m)