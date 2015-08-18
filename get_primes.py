#!/usr/bin/env python
""" Calculates the first NUM_PRIMES prime numbers.
"""
import math as m

NUM_PRIMES = 100000
primes = (2, 3)

def check_if_prime(num):
    num_is_prime = True
    for prime in primes[1: ]: # Skip 2, we're only evaluating odd numbers
        if prime > m.sqrt(num): # https://en.wikipedia.org/wiki/Prime_number says you can stop at sqrt of n
            break
        if num % prime == 0:
            num_is_prime = False
            break
    return num_is_prime

num_to_check = 5
while len(primes) < NUM_PRIMES:
    num_is_prime = check_if_prime(num_to_check)
    if num_is_prime:
        primes += (num_to_check,)
    num_to_check += 2

print "First {} primes\n: {}".format(NUM_PRIMES, primes)

