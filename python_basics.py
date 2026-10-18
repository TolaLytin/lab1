def count_vowels(s: str) -> int:
    vowels = set("aeiouAEIOU")
    return sum(1 for char in s if char in vowels)


def has_unique_characters(s: str) -> bool:
    return len(s) == len(set(s))


def count_one_bits(n: int) -> int:
    return bin(n).count('1')


def multiplicative_persistence(n: int) -> int:
    steps = 0
    while n >= 10:
        prod = 1
        for digit in str(n):
            prod *= int(digit)
        n = prod
        steps += 1
    return steps


def mse(x: list[int], y: list[int]) -> float:
    n = len(x)
    squared_errors = sum((x[i] - y[i]) ** 2 for i in range(n))
    return squared_errors / n


def prime_factorization(n: int) -> str:
    factors = []
    d = 2
    while d * d <= n:
        count = 0
        while n % d == 0:
            n //= d
            count += 1
        if count > 0:
            factors.append((d, count))
        d += 1
    if n > 1:
        factors.append((n, 1))
    
    result = ""
    for base, exp in factors:
        if exp == 1:
            result += f"({base})"
        else:
            result += f"({base}**{exp})"
    return result


def pyramid(n: int) -> int | str:
    k = 1
    current_sum = 0
    while current_sum < n:
        current_sum += k ** 2
        if current_sum == n:
            return k
        k += 1
    return "It is impossible"


def is_balanced_number(n: int) -> bool:
    s = str(n)
    length = len(s)
    mid = length // 2
    
    if length % 2 == 0:
        left_part = s[:mid - 1]
        right_part = s[mid + 1:]
    else:
        left_part = s[:mid]
        right_part = s[mid + 1:]
        
    sum_left = sum(int(c) for c in left_part)
    sum_right = sum(int(c) for c in right_part)
    
    return sum_left == sum_right

if __name__ == "__main__":
    print("Тест 1 (гласные):", count_vowels("Hello World")) # Ожидается 3
    print("Тест 2 (уникальность):", has_unique_characters("abc")) # Ожидается True
    print("Тест 3 (биты):", count_one_bits(7)) # Ожидается 3
    print("Тест 4 (устойчивость):", multiplicative_persistence(39)) # Ожидается 3
    print("Тест 5 (MSE):", mse([1, 2], [3, 4])) # Ожидается 4.0
    print("Тест 6 (множители):", prime_factorization(86240)) # Ожидается (2**5)(5)(7**2)(11)
    print("Тест 7 (пирамида):", pyramid(14)) # Ожидается 3 (1+4+9)
    print("Тест 8 (сбаланс):", is_balanced_number(1234006)) # Ожидается True