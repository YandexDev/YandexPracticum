"""
Метод setUpClass() также предназначен для установки фикстур,
но он вызывается лишь один раз, перед запуском всех test case класса.
Обратите внимание: setUpClass() — это «метод класса» (class method),
его обязательно декорировать, а его первый аргумент должен называться cls.
Для вызова метода класса не требуется создавать объект: такой метод можно вызвать напрямую из класса."""
...


class TestCalc(unittest.TestCase):
    """Тестируем Calculator."""

    @classmethod
    def setUpClass(cls):
        """Вызывается однажды перед запуском всех тестов класса."""
        # Arrange - подготавливаем данные для теста
        cls.calc = MadCalculator()

    def test_sum_string(self):
        act = TestCalc.calc.sum_string(1, 100500)
        self.assertEqual(
            act, 1100500, 'Метод sum_string работает неправильно.'
        )

    def test_sum_string_first_negative_value(self):
        self.assertRaises(ValueError, TestCalc.calc.sum_string, -1, 100500)

    def test_sum_string_second_negative_value(self):
        with self.assertRaises(ValueError):
            TestCalc.calc.sum_string(1, -100500)

    def test_sum_args(self):
        act = TestCalc.calc.sum_args(3, -3, 5)
        self.assertEqual(act, 5, 'Метод sum_args работает неправильно.')


if __name__ == "__main__":
    unittest.main()
