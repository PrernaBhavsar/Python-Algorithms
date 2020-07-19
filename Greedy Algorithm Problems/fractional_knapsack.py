
def get_optimal_value(capacity, weights, values):
    value = 0.
    
    val_unit= [[values[i], weights[i], values[i]/weights[i]] for i in range(len(values))]
    val_unit.sort(key= lambda x: x[2], reverse= True)
    
    values =[item[0] for item in val_unit]
    weights=[item[1] for item in val_unit]
    val= [item[2] for item in val_unit]
    
    for i in range(len(values)):
        
        if capacity== 0:
            return value
        
        a= min([weights[i], capacity])
        value += a*val[i]
        weights[i] -= a
        capacity -= a
              
    return value

if __name__ == "__main__":
    data = list(map(int, input().split()))
    n, capacity = data[0:2]
    values, weights =[], []
    
    for i in range(n):
        data = list(map(int, input().split()))
        values.append(data[0])
        weights.append(data[1])

    
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.3f}".format(opt_value))