# Uses python3
def pisano(m):
    previous =0
    current= 1
    
    for i in range(m*m):
        previous, current = current, (previous + current) % m
        
        if previous == 0 and current == 1:
            return i+1

def get_fibonacci_huge(n, m, pp):
    
    n = n% pp
    
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


n, m = map(int, input().split())
pisano_p= pisano(m)
print(get_fibonacci_huge(n, m, pisano_p))
