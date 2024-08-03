from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self):
        self.car = Vehicle(15.5, 111)

    def test_vehicle_init(self):
        self.assertEqual(15.5, self.car.fuel)
        self.assertEqual(111, self.car.horse_power)
        # self.assertEqual(Vehicle.capacity, self.car.fuel)
        # self.assertEqual(Vehicle.fuel_consumption, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_vehicle_not_enough_fuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(100)

        self.assertEqual('Not enough fuel', str(ex.exception))

    def test_drive_success(self):
        self.car.drive(10)
        self.assertEqual(3, self.car.fuel)

    def test_refuel_too_much_fuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(20)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_success(self):
        self.car.drive(10)
        self.car.refuel(10)

        self.assertEqual(13, self.car.fuel)

    def test_str(self):
        self.assertEqual("The vehicle has 111 horse power with 15.5 fuel left and 1.25 fuel consumption",
                         self.car.__str__())


if __name__ == '__main__':
    main()
