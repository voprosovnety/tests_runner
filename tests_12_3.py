import runner
import unittest
import runner_and_tournament as rnt


class RunnerTest(unittest.TestCase):
    is_frozen=False

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_walk(self):
        walker = runner.Runner('John')
        for i in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_run(self):
        obj_runner = runner.Runner('Steve')
        for i in range(10):
            obj_runner.run()
        self.assertEqual(obj_runner.distance, 100)

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        obj_runner_1 = runner.Runner('Max')
        obj_runner_2 = runner.Runner('Paul')
        for i in range(10):
            obj_runner_2.walk()
            obj_runner_1.run()
        self.assertNotEqual(obj_runner_1.distance, obj_runner_2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen=True
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.usain = rnt.Runner('Усэйн', 10)
        self.andrew = rnt.Runner('Андрей', 9)
        self.nick = rnt.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        print(cls.all_results)

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_tournament_1(self):
        tournament_1 = rnt.Tournament(90, self.usain, self.nick)
        results = tournament_1.start()
        self.assertTrue(results[2] == 'Ник')

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_tournament_2(self):
        tournament_2 = rnt.Tournament(90, self.andrew, self.nick)
        results = tournament_2.start()
        self.assertTrue(results[2] == 'Ник')

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_tournament_3(self):
        tournament_3 = rnt.Tournament(90, self.usain, self.andrew, self.nick)
        results = tournament_3.start()
        self.assertTrue(results[3] == 'Ник')
