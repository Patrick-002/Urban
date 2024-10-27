import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


import unittest

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrei = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for test_name, results in cls.all_results.items():
            print(results)

    def test_usain_and_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        result = tournament.start()
        self.__class__.all_results["Усэйн и Ник"] = {place: str(runner) for place, runner in result.items()}
        self.assertTrue(result[max(result.keys())] == "Ник")

    def test_andrei_and_nick(self):
        tournament = Tournament(90, self.andrei, self.nick)
        result = tournament.start()
        self.__class__.all_results["Андрей и Ник"] = {place: str(runner) for place, runner in result.items()}
        self.assertTrue(result[max(result.keys())] == "Ник")

    def test_usain_andrei_nick(self):
        tournament = Tournament(90, self.usain, self.andrei, self.nick)
        result = tournament.start()
        self.__class__.all_results["Усэйн, Андрей и Ник"] = {place: str(runner) for place, runner in result.items()}
        self.assertTrue(result[max(result.keys())] == "Ник")

if __name__ == "__main__":
    unittest.main()

