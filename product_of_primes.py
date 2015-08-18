#!/usr/bin/env python
"""
From number theory: 
Product of primes less than n is less than or equal to e ** n as n grows.

This script computes the sum of the logarithms of all the primes from 2 to some number n 
(identfied as LARGE_NUM in this script), and prints out the sum of the logs
of the primes, the number n, and the ratio of these two quantities. 
"""

import math as m

LARGE_NUM = 2 ** 20

def get_primes(max_num):
    primes = (2, 3)
    def check_if_prime(num):
        for prime in primes[1: ]: # Skip 2; we're only evaulating odd integers
            num_is_prime = True
            if prime > m.sqrt(max_num): # https://en.wikipedia.org/wiki/Prime_number says you can stop at sqrt of n 
                break
            elif num % prime == 0:
                num_is_prime = False
                break
        return num_is_prime

    num_to_check = 5
    while num_to_check <=  max_num:
        num_is_prime = check_if_prime(num_to_check)
        if num_is_prime:
            primes +=  (num_to_check,)
        num_to_check += 2

    return primes

def get_sum_of_logs_of_primes(primes):
    sum_of_logs = 0
    for prime in primes:
        sum_of_logs += m.log(prime)
    return sum_of_logs

primes = get_primes(LARGE_NUM)
sum_of_logs_of_primes = get_sum_of_logs_of_primes(primes)
print "Sum of logs: {}, n: {}, ratio: {}".format(sum_of_logs_of_primes, 
        LARGE_NUM, sum_of_logs_of_primes / LARGE_NUM)
