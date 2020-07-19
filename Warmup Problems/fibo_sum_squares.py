def pisano(m):
    previous =0
    current= 1
    
    for i in range(m*m):
        previous, current = current, (previous + current) % m
        
        if previous == 0 and current == 1:
            return i+1
        
def fibonacci_sum(n, pp):
    n = n % pp
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):

        previous, current = current , (previous + current) %10 
        sum += (current**2) % 10

    return sum % 10


n = int(input())
pisano_p= pisano(10)
print(fibonacci_sum(n, pisano_p))