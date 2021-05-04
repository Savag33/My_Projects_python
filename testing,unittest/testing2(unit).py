# если название начинаеться на test_ - то етот метод будет отрабативать автоматически только если импортиривали unittest
# assertEqual - сравнивает левую часть с справой! если правая часть ровна левой тогда тест пройден
# тоесть: assertEqual(a, b) — a == b
#
#  assertNotEqual(a, b) — a != b
#
#  assertTrue(x) — bool(x) is True
#
#  assertFalse(x) — bool(x) is False
#
#  assertIs(a, b) — a is b
#
# assertIsNot(a, b) — a is not b
#
# assertIsNone(x) — x is None
#
# assertIsNotNone(x) — x is not None
#
# assertIn(a, b) — a in b
#
# assertNotIn(a, b) — a not in b
#
#
#  setUp() Метод вызывается перед запуском теста. Как правило, используется для подготовки окружения для теста.
#


import unittest
from full_name import full_name

class NameTestCase(unittest.TestCase):

    """Тесты для функции full_name.py"""
    def test_first_last_name(self):

        """Имена вида: Артем Блаженко , тести"""
        format_name = full_name('Артем', 'Блаженко')

        self.assertEqual(format_name,'Артем Блаженко')

    def test_first_last_middle(self):
        """Имена вида: Артем Блаженко Вадимович, тести"""

        format_name = full_name('Артем', 'Блаженко' , 'Вадимович')
        self.assertEqual(format_name, 'Артем Блаженко Вадимович')


if __name__ == '__main__':
    unittest.main()

