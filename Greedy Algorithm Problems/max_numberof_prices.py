def optimal_summands(n):
    summands = []
    i=1
    while n!=0:
        if n>=i and (n-i == 0 or n-i > i) :
            summands.append(i)
            n=n-i
            i+=1
        else:
            i+=1
    return summands

if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)