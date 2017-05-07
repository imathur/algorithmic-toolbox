# Uses python3

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def MinMax(i, j, op, m, M):
    import numpy as np
    m_min = np.inf
    m_max = -np.inf

    for k in range(i, j):
        a = evalt(M[i][k], M[k+1][j], op[k])
        b = evalt(M[i][k], m[k+1][j], op[k])
        c = evalt(m[i][k], M[k+1][j], op[k])
        d = evalt(m[i][k], m[k+1][j], op[k])
        
        m_min = min(m_min, a, b, c, d)
        m_max = max(m_max, a, b, c, d)
    
    return(m_min, m_max)      
        
def get_maximum_value(dataset):
    op = dataset[1 : len(dataset) : 2]
    digits = dataset[0 : len(dataset)+1 : 2]

    n = len(digits)
    m = [[0]*n for _ in range(n)]
    M = [[0]*n for _ in range(n)]

    for i in range(n):
        m[i][i] = int(digits[i])
        M[i][i] = int(digits[i])

    for s in range(1, n):
        for i in range(n-s):
            j = i + s
            m[i][j], M[i][j] = MinMax(i, j, op, m, M)

    return M[0][n-1]

if __name__ == "__main__":
    print(get_maximum_value(input()))
