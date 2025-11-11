from typing import List, Tuple

def sieve(limit: int):
    """метод Эратосфена для поиска простых чисел."""
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return sieve

twin_pairs = []
ratios = []
limit = 10 ** 6

def twin_primes_analysis(limit_pairs: int = 1000) -> Tuple[List[Tuple[int, int]], List[float]]:
    """
    Возвращает:
        - список первых `limit_pairs` пар близнецов (p, p+2);
        - список значений отношения pi_2(n) / pi(n) для n, соответствующих последним
            → элементам каждой пары,
        где pi_2(n) — количество пар близнецов <= n, pi(n) — количество простых <= n.
    """
    twin_pairs = []
    ratios = []
    limit = 10 ** 6

    while len(twin_pairs) < limit_pairs:
        primes_list = [i for i, is_p in enumerate(sieve(limit)) if is_p]
        twins = []
        ratio_vals = []
        twin_count = 0

        for i in range(len(primes_list) - 1):
            if primes_list[i + 1] - primes_list[i] == 2:
                twin_count += 1
                twins.append((primes_list[i], primes_list[i + 1]))
                ratio_vals.append(twin_count / (i + 2))
                if twin_count >= limit_pairs:
                    break

        if len(twins) >= limit_pairs:
            twin_pairs = twins[:limit_pairs]
            ratios = ratio_vals[:limit_pairs]
            break
        else:
            limit *= 2

    return twin_pairs, ratios

def calculate_prime_density(pairs: List[Tuple[int, int]]) -> List[float]:
    """Вычисляет плотность пар близнецов в различных диапазонах."""
    densities = []

    for i in range(0, len(pairs), 100):
        end_idx = min(i + 99, len(pairs) - 1)
        start_prime = pairs[i][0]
        end_prime = pairs[end_idx][1]
        density = 100 / (end_prime - start_prime) if end_prime > start_prime else 0
        densities.append(density)

    return densities

if __name__ == "__main__":
    pairs, ratios = twin_primes_analysis(1000)
    print(f"найдено {len(pairs)} пар")
    print("первая пара:", pairs[0])
    print("последняя пара:", pairs[-1])
    print(f"отношение для последней пары:",ratios[-1])
    densities = calculate_prime_density(pairs)
    for i, density in enumerate(densities):
        print(f"Пары {i * 100 + 1:}-{(i + 1) * 100}: плотность = {density}")
    print("видно что пары близнецов становятся реже с ростом n, а последнее просто случайность из-за выбранного диапазона")