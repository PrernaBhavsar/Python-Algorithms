def compute_min_refills(distance, tank, stops):
    
    val= 0
    current= 0
    x =[0]
    for s in stops:
        x.append(s)
    x.append(distance)
    n = len(x)-2
    
    while current <= n:
        last= current
        
        while current <= n and x[current+1]- x[last] <= tank:
            current +=1
        
        if current == last:
            return -1
        if current <=n:
            val +=1
    
    return val
    
        

if __name__ == '__main__':
    
    d= int(input())
    m= int(input())
    n= int(input())
    stops= map(int, input().split())
    print(compute_min_refills(d, m, stops))