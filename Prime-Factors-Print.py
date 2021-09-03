def is_prime(n):
    for x in range(2, n):
        if n%x==0:
            return False
    else:
        return n

if __name__ == '__main__':
    num = 48
    all_factors = []
    for i in range(2,num):
        if num%i==0:
            all_factors.append(i)
    all_prime_factors = []

    for data in all_factors:
        result = is_prime(data)
        all_prime_factors.append(result)

    for prime in all_prime_factors:
        if prime:
            print(prime)