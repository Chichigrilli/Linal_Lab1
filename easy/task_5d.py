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
    def compute_factorial(n: int) -> int:
        """Вычисляет факториал числа n с кэшированием результатовю"""
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    def find_prime_factors(number: int, prime_numbers: List[int]) -> Dict[int, int]:
        """Находит простые множители числа используя заранее вычисленные простые числа."""
        factors = {}
        remaining = number
        for prime in prime_numbers:
            if prime * prime > remaining:
                break

            if remaining % prime == 0:
                exponent = 0
                while remaining % prime == 0:
                    exponent += 1
                    remaining //= prime
                factors[prime] = exponent
            if remaining == 1:
                break

        if remaining > 1:
            factors[remaining] = 1

        return factors

    def generate_prime_numbers(upper_limit: int) -> List[int]:
        """Генерирует все простые числа до заданного предела используя решето Эратосфена.t"""
        sieve = [True] * (upper_limit + 1)
        sieve[0] = sieve[1] = False
        for current_num in range(2, int(math.sqrt(upper_limit)) + 1):
            if sieve[current_num]:
                for multiple in range(current_num * current_num, upper_limit + 1, current_num):
                    sieve[multiple] = False

        return [num for num in range(2, upper_limit + 1) if sieve[num]]
    prime_list = generate_prime_numbers(10000)
    factorization_results = {}

    for n in range(2, 51):
        factorial_plus_one = compute_factorial(n) + 1
        prime_factors = find_prime_factors(factorial_plus_one, prime_list)
        factorization_results[n] = prime_factors
        print(f"n={n}, n!+1={factorial_plus_one}, множители={prime_factors}")

    return factorization_results


if __name__ == "__main__":
    results = factorial_plus_one_factors()
    print("\nИтоговые результаты:")
    print(results)