from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.m = Mammal('Test', 'Wolf', 'auuuuu')

    def test_mammal_init(self):
        self.assertEqual('Test', self.m.name)
        self.assertEqual('Wolf', self.m.type)
        self.assertEqual('auuuuu', self.m.sound)
        self.assertEqual('animals', self.m.get_kingdom())

    def test_mammal_make_sound(self):
        self.assertEqual('Test makes auuuuu', self.m.make_sound())

    def test_mammal_info(self):
        self.assertEqual('Test is of type Wolf', self.m.info())


if __name__ == "__main__":
    main()
