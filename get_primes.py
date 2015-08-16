#!/usr/bin/env python
"""
"""

primes = [2, 3]

def get_primes(max_num):
    def check_if_prime(num):
        i = 1
        while (i < len(primes)):
            is_prime = True
            if num % primes[i] == 0:
                is_prime = False
                break
            else:
                i += 1
        return is_prime

    num_to_check = 5
    while num_to_check <= max_num:
        is_prime = check_if_prime(num_to_check)
        if is_prime:
            primes.append(num_to_check)
        num_to_check += 2

get_primes(LARGE_NUM)

print primes
print len(primes)


