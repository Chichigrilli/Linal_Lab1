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

    def factorize(n: int) -> Dict[int, int]:
        """Универсальная факторизация без ограничения простыми числами."""
        factors = {}
        temp = n

        # Обрабатываем 2 отдельно для оптимизации
        while temp % 2 == 0:
            factors[2] = factors.get(2, 0) + 1
            temp //= 2

        # Проверяем нечетные делители
        f = 3
        while f * f <= temp:
            if temp % f == 0:
                factors[f] = factors.get(f, 0) + 1
                temp //= f
            else:
                f += 2

        # Если остаток > 1, он простой
        if temp > 1:
            factors[temp] = factors.get(temp, 0) + 1

        return factors

    result = {}

    for n in range(2, 51):
        fact_plus_one = factorial(n) + 1
        factors = factorize(fact_plus_one)
        result[n] = factors
        print(f"{n}: {fact_plus_one} = {factors}")

    return result


# Дополнительная функция для анализа
def analyze_results(results: Dict[int, Dict[int, int]]):
    """Анализирует результаты факторизации."""
    print("\n" + "=" * 60)
    print("АНАЛИЗ РЕЗУЛЬТАТОВ")
    print("=" * 60)

    max_distinct = 0
    n_with_max = []
    large_primes = []

    for n, factors in results.items():
        distinct_count = len(factors)

        # Максимальное количество различных простых делителей
        if distinct_count > max_distinct:
            max_distinct = distinct_count
            n_with_max = [n]
        elif distinct_count == max_distinct:
            n_with_max.append(n)

        # Большие простые множители (> 10^6)
        for prime in factors:
            if prime > 10 ** 6:
                large_primes.append((n, prime))

    print(f"Максимальное количество различных простых делителей: {max_distinct}")
    print(f"Достигается при n = {n_with_max}")

    print(f"\nБольшие простые множители (> 10^6):")
    for n, prime in large_primes:
        print(f"n = {n}: {prime}")


if __name__ == "__main__":
    results = factorial_plus_one_factors()
    analyze_results(results)