import math

def is_prime(n):
    if n < 2:
        return False
    max_num = math.floor(math.sqrt(n))
    for i in range(2, max_num + 1):
        if n % i == 0:
            return False
    return True


print(is_prime(6))
