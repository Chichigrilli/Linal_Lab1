from typing import Dict, List
from palindromes_square import is_prime

def generate_numbers(digits: List[int], limit: int) -> List[int]:
    """генерирует простые числа, состоящие только из указанных чисел"""
    def generate(current: int):
        if current > limit:
            return
        if current > 0 and is_prime(current):
            primes.append(current)
        for digit in digits:
            generate(current * 10 + digit)

    primes = []
    generate(0)
    return sorted(primes)

def primes_with_two_digits() -> Dict[str, List[int]]:
    """возвращающая первые 100 простых чисел для каждого набора цифр"""
    results = {}
    digit_sets = {
        '13': [1, 3],
        '15': [1, 5],
        '17': [1, 7],
        '19': [1, 9]
    }
    for key, digits in digit_sets.items():
        primes = generate_numbers(digits, 1000000)
        results[key] = primes[:100]

    return results


def analyze_type_rarity(results: Dict[str, List[int]]) -> str:
    """функция для анализа"""
    min_count = float('inf')
    rarest_type = ""

    for key, primes in results.items():
        count = len(primes)
        if count < min_count:
            min_count = count
            rarest_type = key
    return f"Тип {rarest_type} встречается реже из-за того, что число не может оканчиваться на 5, так как оно иначе будет делиться на 5 и не будет простым числом, и числа из 1 и 5 часто делятся на 3"

if __name__ == "__main__":
    results = primes_with_two_digits()
    for key, primes in results.items():
        print(f"Первые 100 простых чисел для набора цифр {key}: {primes[:10]}...")  # Печатаем только первые 10 для краткости
    analysis = analyze_type_rarity(results)
    print("\nАнализ редкости типов:")
    print(analysis)