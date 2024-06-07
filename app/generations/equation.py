import random
import sympy as sp


def generate_equation(level):
    if level == 1:
        num = random.randint(1, 10)
        result = random.randint(1, 20)
        return f"x + {num} = {result}", result - num
    elif level == 2:
        num = random.randint(2, 5)
        result = random.randint(10, 50)
        return f"x * {num} = {result}", result / num
    else:  # 3
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        c = random.randint(1, 10)
        # Решение квадратного уравнения через дискриминант
        discriminant = b ** 2 - 4 * a * c
        if discriminant > 0:
            x1 = sp.Rational(-b + sp.sqrt(discriminant), 2 * a)
            x2 = sp.Rational(-b - sp.sqrt(discriminant), 2 * a)
            return f"{a}x^2 + {b}x + {c} = 0", (str(x1), str(x2))
        elif discriminant == 0:
            x = sp.Rational(-b, 2 * a)
            return f"{a}x^2 + {b}x + {c} = 0", x
        else:
            return f"{a}x^2 + {b}x + {c} = 0", "нет реальных корней"
