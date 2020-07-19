# Uses python3
def lcm(a, b):
    least= a if a<b else b 
    for l in range(0, a*b + 1,least):
        if l % a == 0 and l % b == 0 and l != 0:
            return l

    return a*b



a, b = map(int, input().split())
print(lcm(a, b))

