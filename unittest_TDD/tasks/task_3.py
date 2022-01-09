import unittest


class Calculator:
    """Производит арифметические действия."""

    def summ(self, *args):
        """Возвращает сумму принятых аргументов."""
        return sum(i for i in args)


class TestCalc(unittest.TestCase):
    """Тестируем Calculator."""

    @classmethod
    def setUpClass(cls):
        """Вызывается однажды перед запуском всех тестов класса."""
        cls.calc = Calculator()

    def test_summ(self):
        act = TestCalc.calc.summ(3, -3, 5)
        self.assertEqual(act, 5, 'summ работает неправильно')

    # В Unittest есть встроенный метод для проверки на None: assertIsNone(x)
    # Маленькие тесты — это всегда хорошо. Одна проверка — один тест:
    # test_summ_no_argument — что будет, если функция вызвана без аргументов.
    # test_summ_one_argument — что будет, если функция вызвана с одним аргументом.
    def test_summ_no_argument(self):
        act = TestCalc.calc.summ()
        self.assertIsNone(act, 'summ работает неправильно')

    def test_summ_one_argument(self):
        act = TestCalc.calc.summ(1)
        self.assertIsNone(act, 'summ работает неправильно')
