def max_dot_product(a, b):
    value = 0
    a.sort(reverse=True)
    b.sort(reverse =True)
    
    for i in range(len(a)):
        value += a[i]*b[i]
    return value
    

if __name__ == '__main__':
    n= int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(max_dot_product(a,b))
    