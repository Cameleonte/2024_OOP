from project.climbing_robot import ClimbingRobot

from unittest import TestCase, main


class TestClimbingRobot(TestCase):
    ALLOWED_CATEGORIES = ['Mountain', 'Alpine', 'Indoor', 'Bouldering']

    def setUp(self):
        self.robot = ClimbingRobot(
            "Mountain",
            "Destroyer",
            200,
            1000
        )

        self.robot_with_soft = ClimbingRobot(
            "Mountain",
            "Destroyer",
            200,
            1000
        )

        self.robot_with_soft.installed_software = [
            {"name": "Vox", "memory_consumption": 499, "capacity_consumption": 101},
            {"name": "Boom", "memory_consumption": 502, "capacity_consumption": 98}
        ]

    def test_init(self):
        self.assertEqual("Mountain", self.robot.category)
        self.assertEqual('Destroyer', self.robot.part_type)
        self.assertEqual(200, self.robot.capacity)
        self.assertEqual(1000, self.robot.memory)
        self.assertEqual([], self.robot.installed_software)

    def test_category_value_not_in_allowed_categories_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.robot.category = "Invalid"

        self.assertEqual(
            f"Category should be one of {self.ALLOWED_CATEGORIES}",
            str(ex.exception)
        )

    def test_get_used_capacity_expect_success(self):
        expected_result = sum(s['capacity_consumption'] for s in self.robot_with_soft.installed_software)
        result = self.robot_with_soft.get_used_capacity()

        self.assertEqual(expected_result, result)

    def test_get_available_capacity_expect_success(self):
        expected_result = (self.robot.capacity -
                           sum(s['capacity_consumption'] for s in self.robot_with_soft.installed_software))
        result = self.robot_with_soft.get_available_capacity()

        self.assertEqual(expected_result, result)

    def test_get_used_memory_expect_success(self):
        expected_result = sum(s['memory_consumption'] for s in self.robot_with_soft.installed_software)
        result = self.robot_with_soft.get_used_memory()

        self.assertEqual(expected_result, result)

    def test_get_available_memory_expect_success(self):
        expected_result = (self.robot.memory -
                           sum(s['memory_consumption'] for s in self.robot_with_soft.installed_software))
        result = self.robot_with_soft.get_available_memory()

        self.assertEqual(expected_result, result)

    def test_install_software_with_max_equal_values_expect_success(self):
        result = self.robot.install_software(
            {"name": "Vox", "memory_consumption": 1000, "capacity_consumption": 200}
        )
        self.assertEqual("Software 'Vox' successfully installed on Mountain part.", result)
        self.assertEqual(
            [{"name": "Vox", "memory_consumption": 1000, "capacity_consumption": 200}],
            self.robot.installed_software
        )

    def test_install_software_with_less_than_max_values_expect_success(self):
        result = self.robot.install_software(
            {"name": "Vox", "memory_consumption": 100, "capacity_consumption": 20}
        )
        self.assertEqual("Software 'Vox' successfully installed on Mountain part.", result)
        self.assertEqual(
            [{"name": "Vox", "memory_consumption": 100, "capacity_consumption": 20}],
            self.robot.installed_software
        )

    def test_install_software_with_one_value_greater_than_max_values_returns_error_msg(self):
        # required capacity is greater than the available capacity
        result = self.robot.install_software(
            {"name": "Vox", "memory_consumption": 100, "capacity_consumption": 201}
        )
        self.assertEqual("Software 'Vox' cannot be installed on Mountain part.", result)
        self.assertEqual([], self.robot.installed_software)

        # required capacity is greater than the available capacity
        result = self.robot.install_software(
            {"name": "Vox", "memory_consumption": 1002, "capacity_consumption": 2}
        )
        self.assertEqual("Software 'Vox' cannot be installed on Mountain part.", result)
        self.assertEqual([], self.robot.installed_software)

    def test_install_software_with_two_values_greater_than_max_values_returns_error_msg(self):
        result = self.robot.install_software(
            {"name": "Vox", "memory_consumption": 1001, "capacity_consumption": 201}
        )
        self.assertEqual("Software 'Vox' cannot be installed on Mountain part.", result)
        self.assertEqual([], self.robot.installed_software)


if __name__ == '__main__':
    main()
