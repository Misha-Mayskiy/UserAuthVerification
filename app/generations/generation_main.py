from app.generations.equation import generate_equation
from app.generations.inequality import generate_inequality
from app.generations.numerical import generate_numerical

import random
import sympy as sp


# Главная функция для выбора типа и сложности примера
def generate_example(difficulty="", example_type=""):
    if difficulty == "":
        difficulty = random.choice(['легкий', 'средний', 'сложный'])
    if example_type == "":
        example_type = random.choice(['числовые примеры', 'уравнения', 'неравенства'])

    if example_type == 'числовые примеры':
        question, answer = generate_numerical(difficulty)
    elif example_type == 'уравнения':
        question, answer = generate_equation(difficulty)
    else:  # неравенства
        question, answer = generate_inequality(difficulty)

    return question, answer


# Функция для проверки ответа пользователя
def check_answer(user_answer, correct_answer):
    print(str(correct_answer))
    if str(correct_answer) == user_answer.strip():
        return "Правильно!"
    else:
        return "Неправильно."
