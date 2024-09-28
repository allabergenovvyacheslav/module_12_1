"""
Домашнее задание по теме "Методы Юнит-тестирования"
Цель: освоить методы, которые содержит класс TestCase.

Задача:
В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
В этом коде сможете обнаружить дополненный с предыдущей задачи класс Runner и новый класс Tournament.
Изменения в классе Runner:
Появился атрибут speed для определения скорости бегуна.
Метод __eq__ для сравнивания имён бегунов.
Переопределены методы run и walk, теперь изменение дистанции зависит от скорости.
Класс Tournament представляет собой класс соревнований, где есть дистанция, которую нужно пробежать
и список участников. Также присутствует метод start, который реализует логику бега по предложенной
дистанции.

Напишите класс TournamentTest, наследованный от TestCase. В нём реализуйте следующие методы:

setUpClass - метод, где создаётся атрибут класса all_results. Это словарь в который будут сохраняться
результаты всех тестов.

setUp - метод, где создаются 3 объекта:
Бегун по имени Усэйн, со скоростью 10.
Бегун по имени Андрей, со скоростью 9.
Бегун по имени Ник, со скоростью 3.

tearDownClass - метод, где выводятся all_results по очереди в столбец.

Так же методы тестирования забегов, в которых создаётся объект Tournament на дистанцию 90. У объекта
класса Tournament запускается метод start, который возвращает словарь в переменную all_results. В конце
вызывается метод assertTrue, в котором сравниваются последний объект из all_results (брать по
наибольшему ключу) и предполагаемое имя последнего бегуна.

Напишите 3 таких метода, где в забегах участвуют (порядок передачи в объект Tournament соблюсти):
Усэйн и Ник
Андрей и Ник
Усэйн, Андрей и Ник.
Как можно понять: Ник всегда должен быть последним.

Пример результата выполнения тестов:

{1: Усэйн, 2: Ник}
{1: Андрей, 2: Ник}
{1: Андрей, 2: Усэйн, 3: Ник}

Ran 3 tests in 0.001s
OK
"""

import runner_and_tournament as r_and_t
import unittest


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        метод, где создаётся атрибут класса all_results словарь для сохранения результата
        :return:
        """
        cls.all_result = {}

    def setUp(self):
        """
        метод, где создаются 3 объекта:
        Бегун по имени Усэйн, со скоростью 10.
        Бегун по имени Андрей, со скоростью 9.
        Бегун по имени Ник, со скоростью 3.
        :return:
        """
        self.runner_1 = r_and_t.Runner('Усэй', 10)
        self.runner_2 = r_and_t.Runner('Андрей', 9)
        self.runner_3 = r_and_t.Runner('Ник', 3)

    def test_tournament_1(self):
        """
        методы тестирования забегов
        :return:
        """
        self.tour_1 = r_and_t.Tournament(90, self.runner_1, self.runner_3)
        self.all_result = self.tour_1.start()
        self.assertTrue(self.all_result[2], 'Ник')

    def test_tournament_2(self):
        self.tour_2 = r_and_t.Tournament(90, self.runner_2, self.runner_3)
        self.all_result = self.tour_2.start()
        self.assertTrue(self.all_result[2], 'Ник')

    def test_tournament_3(self):
        self.tour_3 = r_and_t.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.all_result = self.tour_3.start()
        self.assertTrue(self.all_result[3], 'Ник')

    def tearDown(self):
        """
        после прохождения тест-кейса вывести на консоль
        :return:
        """
        print(self.all_result)


if __name__ == '__main__':
    unittest.main
