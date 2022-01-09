import unittest


class Calculator:
    """Производит различные арифметические действия."""

    def divider(self, num1, num2):
        """Возвращает результат деления num1 / num2."""
        pass


class TestCalc(unittest.TestCase):
    """Тестируем Calculator."""

    # Подготовьте данные для теста
    @classmethod
    def setUpClass(cls):
        cls.calc = Calculator()

    def test_divider(self):
        act = TestCalc.calc.divider(
            4, 2
        )  # вызовите метод divider с аргументом
        self.assertEqual(act, 2, 'текст, если проверка провалена')

    def test_divider_zero_division(self):
        # Проверьте, что деление на 0 выбрасывает исключение
        with self.assertRaises(ZeroDivisionError):
            TestCalc.calc.divider(4, 0)
