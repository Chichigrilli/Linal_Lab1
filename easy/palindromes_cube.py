from typing import List
from palindromes_square import is_palindrome, is_prime

def palindromic_cubes_and_palindromic_primes() -> tuple[List[int], List[int]]:
    """
    Возвращает:
        tuple:
            - список всех палиндромов a < 100000, для которых a^3 — палиндром;
            - список всех простых p <= 10000, которые являются палиндромами.
    """
    palindromic_cubes = []
    for a in range(1, 100000):
        if is_palindrome(a):
            if is_palindrome(a**3):
                palindromic_cubes.append(a)

    palindromic_primes = []
    for p in range(2, 10001):
        if is_palindrome(p) and is_prime(p):
            palindromic_primes.append(p)

    return palindromic_cubes, palindromic_primes
if __name__ == "__main__":
    palindromic_cubes, palindromic_primes = palindromic_cubes_and_palindromic_primes()
    print("палиндромы куб которых также палиндром, количество:", len(palindromic_cubes))
    print("сами палиндромы",palindromic_cubes)
    print("палиндромические простые числа, количество:", len(palindromic_primes))
    print("сами числа", palindromic_primes)