def factorial(n) :
	e = 1000000007
	fz = 1

	for i in range(1, n + 1):
		fz = (fz * i) % e

	return fz

result = factorial(56)
print(result)