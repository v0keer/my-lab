import math

# --- Базовые операции ---

def add(a: float, b: float) -> float:
    """Сложение двух чисел."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Вычитание второго числа из первого."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Умножение двух чисел."""
    return a * b

def divide(a: float, b: float) -> float:
    """Деление первого числа на второе."""
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b

# --- Продвинутые операции ---

def power(a: float, b: float) -> float:
    """Возведение числа 'a' в степень 'b'."""
    return a ** b

def sqrt(a: float) -> float:
    """Квадратный корень числа. Число должно быть неотрицательным."""
    if a < 0:
        raise ValueError("Нельзя извлечь корень из отрицательного числа")
    return math.sqrt(a)

def factorial(n: int) -> int:
    """Факториал целого неотрицательного числа."""
    if n < 0:
        raise ValueError("Факториал определен только для неотрицательных чисел")
    return math.factorial(n)

# --- Тригонометрия и логарифмы ---

def sin(a: float) -> float:
    """Синус угла (угол передается в радианах)."""
    return math.sin(a)

def cos(a: float) -> float:
    """Косинус угла (угол передается в радианах)."""
    return math.cos(a)

def ln(a: float) -> float:
    """Натуральный логарифм (по основанию e)."""
    if a <= 0:
        raise ValueError("Логарифм определен только для положительных чисел")
    return math.log(a)
