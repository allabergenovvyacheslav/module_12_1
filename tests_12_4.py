import logging
import unittest
import runner_and_tournament_new as rt_new


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        """
        Test for walk function in runner
        :return:
        """
        try:
            jhon = rt_new.Runner('Jhon', -5)
            [jhon.walk() for _ in range(10)]
            self.assertEqual(jhon.distance, 50)
            logging.info(f'{self.test_walk} выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        """
        Test for run function in runner
        :return:
        """
        try:
            bob = rt_new.Runner([1, 2, 3], 10)
            [bob.run() for _ in range(10)]
            self.assertEqual(bob.distance, 100)
            logging.info(f'{self.test_run} выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)


logging.basicConfig(level=logging.INFO,
                    handlers=[logging.FileHandler('runner_tests.log', 'w', 'utf-8')],
                    format='%(asctime)s | %(levelname)s | %(message)s')
