def is_prime(funk):
    def wrapper(a, b, c):
        result = funk(a, b, c)
        is_prime = True
        for i in range(2, result):
            if result % i == 0:
                is_prime = False
        if is_prime:
            print('Простое')
        elif is_prime == False:
            print('Составное')
        return result
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a+b+c


if __name__ == '__main__':
    result = sum_three(2, 3, 6)
    print(result)
