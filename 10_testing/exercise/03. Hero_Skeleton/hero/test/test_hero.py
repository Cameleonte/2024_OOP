from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):

    def setUp(self):
        self.hero = Hero('BamBam', 13, 200, 15)
        self.enemy = Hero('Bum', 10, 200, 14)
        self.player_damage = self.hero.damage * self.hero.level
        self.enemy_damage = self.enemy.damage * self.enemy.level

    def test_init(self):
        self.assertEqual('BamBam', self.hero.username)
        self.assertEqual(13, self.hero.level)
        self.assertEqual(200, self.hero.health)
        self.assertEqual(15, self.hero.damage)

    def test_battle_fight_yourself_raises(self):
        self.enemy.username = 'BamBam'

        self.assertEqual('BamBam', self.hero.username)
        self.assertEqual(200, self.hero.health)

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

        self.assertEqual('BamBam', self.hero.username)
        self.assertEqual(200, self.hero.health)

    def test_battle_with_hero_health_0_raises(self):
        self.hero.health = 0

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

        self.assertEqual(0, self.hero.health)

    def test_battle_with_hero_health_less_than_0_raises(self):
        self.hero.health = -1

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

        self.assertEqual(-1, self.hero.health)

    def test_battle_with_enemy_health_0_raises(self):
        self.enemy.health = 0

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("You cannot fight Bum. He needs to rest", str(ex.exception))

        self.assertEqual(0, self.enemy.health)

    def test_battle_with_enemy_health_less_than_0_raises(self):
        self.enemy.health = -1

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("You cannot fight Bum. He needs to rest", str(ex.exception))

        self.assertEqual(-1, self.enemy.health)

    def test_battle_player_damage(self):

        self.assertEqual(195, self.player_damage)

    def test_battle_enemy_damage(self):

        self.assertEqual(140, self.enemy_damage)

    def test_battle_player_enemy_wins_returns_you_lose(self):
        self.assertEqual(200, self.hero.health)
        self.assertEqual(200, self.enemy.health)
        self.assertEqual(10, self.enemy.level)
        self.assertEqual(14, self.enemy.damage)

        result = self.hero.battle(self.enemy)

        self.assertEqual("You lose", result)

        self.assertEqual(11, self.enemy.level)
        self.assertEqual(19, self.enemy.damage)
        self.assertEqual(60, self.hero.health)
        self.assertEqual(10, self.enemy.health)

    def test_battle_player_hero_wins_enemy_health_equal_0_returns_you_win(self):
        self.enemy.health = 195
        self.assertEqual(200, self.hero.health)
        self.assertEqual(13, self.hero.level)
        self.assertEqual(15, self.hero.damage)

        result = self.hero.battle(self.enemy)

        self.assertEqual("You win", result)

        self.assertEqual(14, self.hero.level)
        self.assertEqual(20, self.hero.damage)
        self.assertEqual(65, self.hero.health)
        self.assertEqual(0, self.enemy.health)

    def test_battle_player_hero_wins_enemy_health_minor_0_returns_you_win(self):
        self.enemy.health = 190
        self.assertEqual(200, self.hero.health)
        self.assertEqual(13, self.hero.level)
        self.assertEqual(15, self.hero.damage)

        result = self.hero.battle(self.enemy)

        self.assertEqual("You win", result)

        self.assertEqual(14, self.hero.level)
        self.assertEqual(20, self.hero.damage)
        self.assertEqual(65, self.hero.health)
        self.assertEqual(-5, self.enemy.health)

    def test_battle_both_players_health_is_0(self):
        self.hero.level, self.hero.damage = 20, 10
        self.enemy.level, self.enemy.damage = 10, 20

        self.assertEqual('Draw', self.hero.battle(self.enemy))

        self.assertEqual(0, self.hero.health)
        self.assertEqual(0, self.enemy.health)

    def test_battle_both_players_health_is_less_than_0(self):
        self.hero.level, self.hero.damage = 20, 11
        self.enemy.level, self.enemy.damage = 11, 20

        self.assertEqual('Draw', self.hero.battle(self.enemy))

        self.assertEqual(-20, self.hero.health)
        self.assertEqual(-20, self.enemy.health)

    def test_battle_str(self):
        self.assertEqual("Hero BamBam: 13 lvl\nHealth: 200\nDamage: 15\n", self.hero.__str__())


if __name__ == '__main__':
    main()
