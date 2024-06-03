import random


def generate_numerical(level):
    operations = ['+', '-', '*', '/']
    if level == 'легкий':
        num1, num2 = random.randint(1, 10), random.randint(1, 10)
    elif level == 'средний':
        num1, num2 = random.randint(10, 50), random.randint(10, 50)
    else:  # сложный
        num1, num2 = random.randint(50, 100), random.randint(50, 100)
    operation = random.choice(operations)
    question = f"{num1} {operation} {num2}"

    # Обработка операции деления
    if operation == '/':
        # Проверка на целочисленное деление
        if num1 % num2 == 0:
            answer = num1 // num2
        else:
            # Округление до двух знаков после запятой
            answer = round(num1 / num2, 2)
    else:
        answer = eval(question)

    return question, answer
