import random
import sympy as sp


def generate_inequality(level):
    signs = ['<', '>', '<=', '>=']
    if level == 'легкий':
        num = random.randint(1, 10)
        result = random.randint(1, 20)
        sign = random.choice(signs)
        return f"x + {num} {sign} {result}", f"x {sign} {result - num}"
    elif level == 'средний':
        num = random.randint(2, 5)
        result = random.randint(10, 50)
        sign = random.choice(signs)
        return f"x * {num} {sign} {result}", f"x {sign} {result // num}"
    else:  # сложный
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        c = random.randint(1, 10)
        sign = random.choice(['<', '>', '<=', '>='])
        # Решение квадратного неравенства через дискриминант
        discriminant = b ** 2 - 4 * a * c
        if discriminant >= 0:
            x1 = sp.Rational(-b + sp.sqrt(discriminant), 2 * a)
            x2 = sp.Rational(-b - sp.sqrt(discriminant), 2 * a)
            if a > 0:
                if sign in ['>', '>=']:
                    return f"{a}x^2 + {b}x + {c} {sign} 0", f"x < {x1} или x > {x2}"
                else:
                    return f"{a}x^2 + {b}x + {c} {sign} 0", f"{x1} < x < {x2}"
            else:
                if sign in ['>', '>=']:
                    return f"{a}x^2 + {b}x + {c} {sign} 0", "нет решения"
                else:
                    return f"{a}x^2 + {b}x + {c} {sign} 0", "все x"
        else:
            if a > 0:
                if sign in ['>', '>=']:
                    return f"{a}x^2 + {b}x + {c} {sign} 0", "все x"
                else:
                    return f"{a}x^2 + {b}x + {c} {sign} 0", "нет решения"
            else:
                if sign in ['>', '>=']:
                    return f"{a}x^2 + {b}x + {c} {sign} 0", "нет решения"
                else:
                    return f"{a}x^2 + {b}x + {c} {sign} 0", "все x"
