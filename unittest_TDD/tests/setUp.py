"""
Для создания фикстур чаще всего используют метод setUp().
Это встроенный метод Unittest, он автоматически вызывается перед запуском каждого test case:"""


class TestCalc(unittest.TestCase):
    """Тестируем Calculator."""

    def setUp(self):
        """Подготовка прогона теста. Вызывается перед каждым тестом."""
        # Arrange - подготавливаем данные для теста
        self.calc = MadCalculator()

    def test_sum_args(self):
        act = self.calc.sum_args(3, -3, 5)
        self.assertEqual(act, 5, 'Метод sum_args работает неправильно.')

    # Другие test case
    ...


...
