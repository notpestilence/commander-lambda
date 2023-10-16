def solution(x, y):
    # Find x-axis by general triangular number formula 
    tn = (x * (x + 1)) / 2 

    # Find y-axis by arithmetic sequence
    for i in range(int(y) - 1): 
        tn += i + x
    
    return(str(int(tn)))