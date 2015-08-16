#!/usr/bin/env python
"""
From number theory: 
Product of primes less than n is less than or equal to e ** n as n grows.

This script computes the sum of the logarithms of all the primes from 2 to some number n 
(identfied as LARGE_NUM in this script), and prints out the sum of the logs
of the primes, the number n, and the ratio of these two quantities. 
"""

import math as m

#LARGE_NUM = 100000
LARGE_NUM = 2 ** 18

def get_primes(max_num):
    primes = [2, 3]
    counter = 0
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
#        print "Checking {}".format(num_to_check)
        is_prime = check_if_prime(num_to_check)
        if is_prime:
            primes.append(num_to_check)
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

print len(primes)


