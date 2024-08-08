from unittest import TestCase, main

from project.robot import Robot


class TestRobot(TestCase):

    def setUp(self):
        self.my_robot = Robot('A1', 'Military', 500, 10000)
        self.oth_robot = Robot('O1', 'Entertainment', 800, 5000)

    def test_init(self):
        self.assertEqual(self.my_robot.robot_id, 'A1')
        self.assertEqual(self.my_robot.category, 'Military')
        self.assertEqual(self.my_robot.available_capacity, 500)
        self.assertEqual(self.my_robot.price, 10000)
        self.assertEqual(self.my_robot.hardware_upgrades, [])
        self.assertEqual(self.my_robot.software_updates, [])

        self.assertEqual('O1', self.oth_robot.robot_id)
        self.assertEqual('Entertainment', self.oth_robot.category)
        self.assertEqual(800, self.oth_robot.available_capacity)
        self.assertEqual(5000, self.oth_robot.price)
        self.assertEqual([], self.oth_robot.hardware_upgrades)
        self.assertEqual([], self.oth_robot.software_updates)

    def test_wrong_category_raises(self):
        with self.assertRaises(Exception) as ex:
            self.my_robot = Robot('A1', 'Niente', 500, 10000)
            self.oth_robot = Robot('O1', 'pi4', 800, 5000)

            self.assertEqual(str(ex.exception),
                             "Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'")

        self.my_robot = Robot('A1', 'Military', 500, 10000)
        self.oth_robot = Robot('O1', 'Entertainment', 800, 5000)

    def test_negative_price_raises(self):
        with self.assertRaises(Exception) as ex:
            self.my_robot = Robot('A1', 'Military', 500, - 3)
            self.oth_robot = Robot('O1', 'Entertainment', 800, - 1)

            self.assertEqual(str(ex.exception), "Price cannot be negative!")

        self.my_robot = Robot('A1', 'Military', 500, 10000)
        self.oth_robot = Robot('O1', 'Entertainment', 800, 5000)

    def test_existent_hardware_component(self):
        self.my_robot.hardware_upgrades.append('Upgraded Mainboard')
        self.my_robot.price = 10000

        result = self.my_robot.upgrade('Upgraded Mainboard', 100)

        self.assertEqual(self.my_robot.hardware_upgrades, ['Upgraded Mainboard'])
        self.my_robot.price = 10000
        self.assertEqual(result, "Robot A1 was not upgraded.")

    def test_hardware_component_upgrade_success(self):
        self.assertEqual(self.my_robot.hardware_upgrades, [])
        self.assertEqual(self.my_robot.price, 10000)

        result = self.my_robot.upgrade('Upgraded Mainboard', 100)

        self.assertEqual(self.my_robot.price, 10150.0)
        self.assertEqual(self.my_robot.hardware_upgrades, ['Upgraded Mainboard'])
        self.assertEqual(result, "Robot A1 was upgraded with Upgraded Mainboard.")

    def test_update_but_not_updates_yet(self):
        self.assertEqual(self.my_robot.software_updates, [])

        result = self.my_robot.update(2.3, 1000)

        self.assertEqual(self.my_robot.software_updates, [])
        self.assertEqual(result, "Robot A1 was not updated.")

    def test_version_older_that_the_current_and_available_capacity_guaranteed(self):
        self.my_robot.software_updates.append(1.1)
        self.assertEqual(self.my_robot.available_capacity, 500)
        self.assertEqual(self.my_robot.software_updates, [1.1])

        result = self.my_robot.update(1.0, 150)

        self.assertEqual(self.my_robot.available_capacity, 500)
        self.assertEqual(self.my_robot.software_updates, [1.1])
        self.assertEqual(result, "Robot A1 was not updated.")

    def test_version_newer_that_the_current_and_available_capacity_not_enough(self):
        self.my_robot.software_updates.append(1.1)
        self.assertEqual(500, self.my_robot.available_capacity)
        self.assertEqual([1.1], self.my_robot.software_updates)

        result = self.my_robot.update(1.2, 650)

        self.assertEqual(500, self.my_robot.available_capacity)
        self.assertEqual([1.1], self.my_robot.software_updates)
        self.assertEqual("Robot A1 was not updated.", result)

    def test_version_newer_that_the_current_and_enough_available_capacity(self):
        self.my_robot.software_updates.append(2.0)
        self.assertEqual(500, self.my_robot.available_capacity)
        self.assertEqual([2.0], self.my_robot.software_updates)

        result = self.my_robot.update(2.2, 450)

        self.assertEqual(50, self.my_robot.available_capacity)
        self.assertEqual([2.0, 2.2], self.my_robot.software_updates)
        self.assertEqual("Robot A1 was updated to version 2.2.", result)

    def test_greater_price_from_other_robot(self):
        self.assertEqual(10000, self.my_robot.price)
        self.assertEqual(5000, self.oth_robot.price)

        result = self.my_robot.__gt__(self.oth_robot)

        self.assertEqual(10000, self.my_robot.price)
        self.assertEqual(5000, self.oth_robot.price)
        self.assertEqual(result, 'Robot with ID A1 is more expensive than Robot with ID O1.')

    def test_equal_price_with_other_robot(self):
        self.oth_robot.price = 10000
        self.assertEqual(10000, self.my_robot.price)
        self.assertEqual(10000, self.oth_robot.price)

        result = self.my_robot.__gt__(self.oth_robot)

        self.assertEqual(10000, self.my_robot.price)
        self.assertEqual(10000, self.oth_robot.price)
        self.assertEqual(result, 'Robot with ID A1 costs equal to Robot with ID O1.')

    def test_cheaper_price_to_other_robot(self):
        self.my_robot.price = 2000
        self.assertEqual(2000, self.my_robot.price)
        self.assertEqual(5000, self.oth_robot.price)

        result = self.my_robot.__gt__(self.oth_robot)

        self.assertEqual(2000, self.my_robot.price)
        self.assertEqual(5000, self.oth_robot.price)
        self.assertEqual(result, 'Robot with ID A1 is cheaper than Robot with ID O1.')


if __name__ == '__main__':
    main()
