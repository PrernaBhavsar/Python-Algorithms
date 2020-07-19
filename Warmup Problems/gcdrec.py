def gcd(x,y):
	if y == 0:
		return x
	else:
		x= x%y
		return gcd(y,x)


a, b = map(int, input().split())
print(gcd(a,b))
