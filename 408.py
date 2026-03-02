def is_prime(x):
    for i in range(2,x):
        if x % i==0:
            return False
            break
    else:
        if x > 1:
            return True
        else:
            return False

def prime_generator(n):
    for i in range(2, n + 1):
        if is_prime(i):
            yield i


n = int(input())
print(*prime_generator(n))