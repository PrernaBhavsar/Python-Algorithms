
def max_pairwise_product(numbers):
    n = len(numbers)
    max1= -1
    max2= -1
    for i in range(n):
        if max1== -1 or numbers[max1]<numbers[i]:
            max1= i
            
    for j in range(n):
        if max1!= j and (max2== -1 or numbers[max2]<numbers[j]):
            max2= j

    return numbers[max1]*numbers[max2]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
