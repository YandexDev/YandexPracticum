from math import sqrt

message = (
    "Добро пожаловать в самую лучшую программу "
    "для вычисления квадратного корня из заданного числа"
)


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Выводит значение квадратного корня."""
    if your_number <= 0:
        return

    root = calculate_square_root(your_number)
    print(
        "Мы вычислили корень квадратный " f"из введенного вами числа. Это будет: {root}"
    )


print(message)
calc(25.5)
