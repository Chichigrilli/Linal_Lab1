from typing import List
def is_palindrome(n: int) -> bool:
    """проверяет, является ли число палиндромом"""
    s = str(n)
    return s == s[::-1]

def is_prime(n: int) -> bool:
    """проверяет, является ли число простым"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_permutations(n: int) -> List[int]:
    """позвращает все циклические перестановки числа"""
    s = str(n)
    permutations = []
    for i in range(len(s)):
        permutation = int(s[i:] + s[:i])
        permutations.append(permutation)

    return permutations

def palindromic_squares_and_circular_primes() -> tuple[List[int], List[int]]:
    """
    Возвращает:
        tuple:
            - список всех палиндромов a < 100000, для которых a^2 — палиндром;
            - список всех простых p < 1000000, все циклические перестановки цифр которых
    """
    palindromic_squares = []
    for a in range(1, 100000):
        if is_palindrome(a):
            if is_palindrome(a * a):
                palindromic_squares.append(a)

    circular_primes = []
    for p in range(2, 1000000):
        if is_prime(p):
            all_prime = True
            for perm in get_permutations(p):
                if not is_prime(perm):
                    all_prime = False
                    break
            if all_prime:
                circular_primes.append(p)

    return palindromic_squares, circular_primes

if __name__ == "__main__":
    palindromic_squares, circular_primes = palindromic_squares_and_circular_primes()
    print("палиндромы квадрат которых также палиндром, количество:", len(palindromic_squares))
    print("сами палиндромы", palindromic_squares)
    print("простые числа все циклические перестановки цифр которых также являются простыми, количество:", len(circular_primes))
    print("сами числа", circular_primes)