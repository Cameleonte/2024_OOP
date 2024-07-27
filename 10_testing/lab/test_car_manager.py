from lab.car_manager import Car

from unittest import TestCase, main


class TestCar(TestCase):
    def setUp(self):
        self.car = Car('Toyota', 'X', 3, 29)

    def test_init(self):
        self.assertEqual("Toyota", self.car.make)
        self.assertEqual('X', self.car.model)
        self.assertEqual(3, self.car.fuel_consumption)
        self.assertEqual(29, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_car_set_make_empty_string_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_car_set_model_empty_string_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_car_set_fuel_consumption_zero_or_negative_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

        # Test consumption less than 0
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = - 3

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_car_set_fuel_capacity_zero_or_negative_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

        # Test consumption less than 0
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = - 1

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_car_set_fuel_amount_negative_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = - 1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_with_zero_or_negative_amount_raises(self):
        refuel_amount = 0
        self.assertEqual(0, self.car.fuel_amount)
        with self.assertRaises(Exception) as ex:
            self.car.refuel(refuel_amount)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))
        self.assertEqual(0, self.car.fuel_amount)

        # Negative amount of refuel
        refuel_amount = - 1
        self.assertEqual(0, self.car.fuel_amount)
        with self.assertRaises(Exception) as ex:
            self.car.refuel(refuel_amount)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))
        self.assertEqual(0, self.car.fuel_amount)

    def test_car_refuel_with_positive_amount_less_than_capacity(self):
        refuel_amount = 10
        self.assertEqual(0, self.car.fuel_amount)
        self.car.refuel(refuel_amount)

        self.assertEqual(10, self.car.fuel_amount)

        self.car.refuel(refuel_amount)

        self.assertEqual(20, self.car.fuel_amount)

    def test_car_refuel_with_amount_more_than_capacity(self):
        refuel_amount = self.car.fuel_capacity + 1
        self.assertEqual(0, self.car.fuel_amount)
        self.car.refuel(refuel_amount)

        self.assertEqual(self.car.fuel_capacity, self.car.fuel_amount)

    def test_drive_with_needed_more_than_fuel_amount_raises(self):
        self.assertEqual(0, self.car.fuel_amount)
        needed = (50 / 100) * self.car.fuel_consumption
        needed += 1

        with self.assertRaises(Exception) as ex:
            self.car.drive(50)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

        self.assertEqual(0, self.car.fuel_amount)

    def test_drive(self):
        refuel_amount = 5
        self.car.refuel(refuel_amount)
        drive_distance = 100
        self.assertEqual(refuel_amount, self.car.fuel_amount)
        needed = (drive_distance / 100) * self.car.fuel_consumption

        self.car.drive(drive_distance)
        expected = refuel_amount - needed
        self.assertEqual(expected, self.car.fuel_amount)


if __name__ == '__main__':
    main()
