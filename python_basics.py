def count_vowels(s: str) -> int:
    vowels = set("aeiouAEIOU")
    return sum(1 for char in s if char in vowels)


def has_unique_characters(s: str) -> bool:
    return len(s) == len(set(s))


def count_one_bits(n: int) -> int:
    # Более быстрый и "питоничный" способ: перевести в строку двоичного представления и посчитать '1'
    return bin(n).count('1')
    # Альтернатива через побитовые операции:
    # count = 0
    # while n > 0:
    #     count += n & 1
    #     n >>= 1
    # return count


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
    # По условию вектора целочисленные, но результат должен быть float
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
    # Ищем k такое, что сумма квадратов 1..k == n
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
    
    left_part = s[:mid]
    # Если длина чётная, то в правую часть берём с mid + 1? Нет.
    # По условию: чётная длина - две средние цифры не входят.
    # Значит, для чётной: left = s[:mid], right = s[mid+1:] ??? 
    # Нет, если длина 6, то индексы 0,1,2,3,4,5. mid = 3. 
    # Две средние цифры - это индексы 2 и 3. 
    # Значит left = s[:2], right = s[4:]. 
    # Если длина нечётная (7), mid = 3. Средняя цифра - индекс 3. 
    # left = s[:3], right = s[4:].
    
    if length % 2 == 0:
        left_part = s[:mid - 1]
        right_part = s[mid + 1:]
    else:
        left_part = s[:mid]
        right_part = s[mid + 1:]
        
    sum_left = sum(int(c) for c in left_part)
    sum_right = sum(int(c) for c in right_part)
    
    return sum_left == sum_right