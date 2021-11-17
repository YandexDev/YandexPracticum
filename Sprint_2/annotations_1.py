name: str = 'Rigard'
age: int = 24
man: bool = True

print(__annotations__)


def foo(names: str, ages: int) -> None:
    print(f'{names} {ages} old!')


foo('Andrei', 35)

print(foo.__annotations__)


# В классе Hello инциализирована строчная переменная x
# со значением по умолчанию 'привет'.
# self в классах никогда не аннотируется.
# __init__ ничего не возвращает.
class Hello:
    x: str  # Если здесь не указывать тип переменной,
    # аннотация для x не отобразится в словаре __annotations__,
    # однако анализатор возьмёт аннотацию из __init__ и корректно отработает

    def __init__(self, x: str = 'Привет') -> None:
        self.x = x


# Вывод на экран словаря __annotations__ из области видимости класса Hello
print(Hello.__annotations__)
