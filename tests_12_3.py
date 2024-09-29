import runner
import unittest
import runner_and_tournament as r_and_t


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        """
        Test for walk function in runner
        :return:
        """
        jhon = runner.Runner('Jhon')
        [jhon.walk() for _ in range(10)]
        self.assertEqual(jhon.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        """
        Test for run function in runner
        :return:
        """
        bob = runner.Runner('Bob')
        [bob.run() for _ in range(10)]
        self.assertEqual(bob.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
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
    var = unittest.main


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        """
        Метод, где создаётся атрибут класса all_results словарь для сохранения результата
        :return:
        """
        cls.all_result = {}

    def setUp(self):
        """
        Метод, где создаются 3 объекта:
        Бегун по имени Усэйн, со скоростью 10.
        Бегун по имени Андрей, со скоростью 9.
        Бегун по имени Ник, со скоростью 3.
        :return:
        """
        self.runner_1 = r_and_t.Runner('Усэй', 10)
        self.runner_2 = r_and_t.Runner('Андрей', 9)
        self.runner_3 = r_and_t.Runner('Ник', 3)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournament_1(self):
        """
        Методы тестирования забегов
        :return:
        """
        self.tour_1 = r_and_t.Tournament(90, self.runner_1, self.runner_3)
        self.all_result = self.tour_1.start()
        self.assertTrue(self.all_result[2], 'Ник')

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournament_2(self):
        """
        Методы тестирования забегов
        :return:
        """
        self.tour_2 = r_and_t.Tournament(90, self.runner_2, self.runner_3)
        self.all_result = self.tour_2.start()
        self.assertTrue(self.all_result[2], 'Ник')

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournament_3(self):
        """
        Методы тестирования забегов
        :return:
        """
        self.tour_3 = r_and_t.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.all_result = self.tour_3.start()
        self.assertTrue(self.all_result[3], 'Ник')

    def tearDown(self):
        """
        После прохождения тест-кейса вывести на консоль
        :return:
        """
        print(self.all_result)


if __name__ == '__main__':
    var = unittest.main
