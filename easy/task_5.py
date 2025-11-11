from typing import Dict, List
import math
from functools import lru_cache

def factorial_plus_one_factors() -> Dict[int, Dict[int, int]]:
    """
        Возвращает словарь вида:
        { n: {простой_делитель: степень, ...}, ... }
        для n от 2 до 50, где ключ — n, значение — разложение n! + 1 на простые множители.
    """


    @lru_cache(maxsize=None)
    def factorial(n: int) -> int:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    # Разложерие на простые множители
    def factorize(n: int, primes: List[int]) -> Dict[int, int]:
        factors = {}
        temp = n

        # Проверяем только простые делители из списка
        for p in primes:
            if p * p > temp:
                break
            if temp % p == 0:
                count = 0
                while temp % p == 0:
                    count += 1
                    temp //= p
                factors[p] = count
            if temp == 1:
                break

        # Если остался простой делитель > 1
        if temp > 1:
            factors[temp] = 1

        return factors

    # Заранее вычисляем все простые числа до 10000
    def generate_primes(limit: int) -> List[int]:
        sieve = [True] * (limit + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(math.sqrt(limit)) + 1):
            if sieve[i]:
                for j in range(i * i, limit + 1, i):
                    sieve[j] = False
        return [i for i in range(2, limit + 1) if sieve[i]]

    primes = generate_primes(10000)
    result = {}

    for n in range(2, 51):
        fact_plus_one = factorial(n) + 1
        factors = factorize(fact_plus_one, primes)
        result[n] = factors
        print(n, factorial(n)+1, result[n] )

print(factorial_plus_one_factors())