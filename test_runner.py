"""
Домашнее задание по теме "Простые Юнит-Тесты"

Цель: приобрести навык создания простейших Юнит-тестов

Задача "Проверка на выносливость":
В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
В этом коде сможете обнаружить класс Runner, объекты которого вам будет необходимо протестировать.

Напишите класс RunnerTest, наследуемый от TestCase из модуля unittest. В классе пропишите следующие
методы:
test_walk - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите
метод walk у этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта
со значением 50.
test_run - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите
метод run у этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта
со значением 100.
test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами. Далее
10 раз у объектов вызываются методы run и walk соответственно. Т.к. дистанции должны быть разными,
используйте метод assertNotEqual, чтобы убедится в неравенстве результатов.
Запустите кейс RunnerTest. В конечном итоге все 3 теста должны пройти проверку.

Пункты задачи:
Скачайте исходный код для тестов.
Создайте класс RunnerTest и соответствующие описанию методы.
Запустите RunnerTest и убедитесь в правильности результатов.
Пример результата выполнения программы:
Вывод на консоль:
Ran 3 tests in 0.001s OK

Примечания:
Попробуйте поменять значения в одном из тестов, результаты
"""

import runner
from unittest import TestCase


class RunnerTest(TestCase):

    def test_walk(self):
        """
        Test for walk function in runner
        :return:
        """
        jhon = runner.Runner('Jhon')
        jhon.walk()
        jhon.walk()
        jhon.walk()
        jhon.walk()
        jhon.walk()
        jhon.walk()
        jhon.walk()
        jhon.walk()
        jhon.walk()
        jhon.walk()
        self.assertEqual(jhon.distance, 50)
        # self.assertEqual(a.distance, 40) -> тест не пройден 50 != 40

    def test_run(self):
        """
        Test for run function in runner
        :return:
        """
        bob = runner.Runner('Bob')
        [bob.run() for _ in range(10)]
        self.assertEqual(bob.distance, 100)

    def test_challenge(self):
        """
        Test for walk != run function in runner
        :return:
        """
        dony = runner.Runner('Dony')
        [dony.walk() for _ in range(10)]
        jhony = runner.Runner('Jhony')
        [jhony.run() for _ in range(10)]
        self.assertNotEqual(dony.distance, jhony.distance)


if __name__ == '__main__':
    unittest.main
