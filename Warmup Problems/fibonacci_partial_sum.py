def pisano(m):
    previous =0
    current= 1
    
    for i in range(m*m):
        previous, current = current, (previous + current) % m
        
        if previous == 0 and current == 1:
            return i+1

def fibonacci_partial_sum(m,n, pisano_p):
    sum = 0
    prev = 0
    curr = 1
    m= m % pisano_p
    n= n % pisano_p
    
    if m<=n:
    
        for i in range(n+1):
            
            if i >= m:
                sum = sum + prev % 10
    
            prev, curr= curr , (prev+curr) % 10
            
    else:
        
        for i in range(pisano_p):
            if i >= m:
                sum = sum + prev % 10
    
            prev, curr= curr , (prev+curr) % 10
        
        for i in range(n+1):
            sum = sum + prev % 10
            prev, curr= curr , (prev+curr) % 10
            

    return sum % 10



m,n = map(int, input().split())
pisano_p = pisano(10)
print(fibonacci_partial_sum(m,n, pisano_p))