# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# print(numbers)

# primes = list()
# not_primes = list()
#

# Cамый домгий и мутврный путь для решения задачи
# for i in numbers:
#    if i % 2 == 0 and i != 6 and i != 4 and i != 8 and i != 14and i != 12 and i != 10:
#        primes.append(i)
#    if i % 3 == 0 and i != 15 and i != 6 and i != 12 and i != 9:
#        primes.append(i)
#    if i % 5 == 0 and i !=15 and i !=10:
#        primes.append(i)
#    if i % 7 == 0 and i != 14:
#        primes.append(i)
#    if i % 11 == 0:
#        primes.append(i)
#    if i % 13 == 0:
#        primes.append(i)
# print("primes:",primes)
#
# for j in numbers:
#    if j % 2 == 0 and j != 2 and j != 6:
#        not_primes.append(j)
#    if j % 3 == 0 and j != 15 and j != 3 and j != 12:
#        not_primes.append(j)
#        if j % 7 == 0:
#            not_primes.append(j)
#    if j % 15 == 0:
#        not_primes.append(j)
# print("not_primes:",not_primes)
#


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for num in numbers:
    if num != 1:
        is_prime = True
        for divisor in range(2, num):
            if num % divisor == 0:
                is_prime = False
        if is_prime:
            primes.append(num)
        else:
            not_primes.append(num)
print("primes: ", primes)
print("not_primes: ", not_primes)