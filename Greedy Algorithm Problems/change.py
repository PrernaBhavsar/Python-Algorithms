
def get_change(m):
    #write your code here
    num_coins=0
    
    while m >0:
        
        if (m-10) >=0:
            num_coins +=1
            m=m-10
            continue
        
        elif (m-5) >=0:
            num_coins +=1
            m=m-5
            continue
        
        elif (m-1) >=0:
            num_coins +=1
            m=m-1
    return num_coins
            
            

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))