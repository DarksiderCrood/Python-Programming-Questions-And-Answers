def countMinStepsToOne(n) :
	if n == 1:
		return 0
	a = 100000
	b = 100000
	c = 100000
	a = countMinStepsToOne(n-1)
	if n%2==0:
		b = countMinStepsToOne(n/2)
	if n%3==0:
		c = countMinStepsToOne(n/3)
	return 1+ min(a,b,c)

result = countMinStepsToOne(99)
print(result)