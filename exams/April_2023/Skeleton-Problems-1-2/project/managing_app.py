from typing import List

from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:

    VALID_VEHICLE_TYPES = {
        'PassengerCar': PassengerCar,
        'CargoVan': CargoVan
    }

    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []

    def __define_next_route(self) -> int:
        next_route = len(self.routes) + 1
        return next_route

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        try:
            existing_user = [u for u in self.users if u.driving_license_number == driving_license_number][0]
            return f"{driving_license_number} has already been registered to our platform."
        except IndexError:
            user = User(first_name, last_name, driving_license_number)
            self.users.append(user)
            return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if not self.VALID_VEHICLE_TYPES.get(vehicle_type):
            return f"Vehicle type {vehicle_type} is inaccessible."
        try:
            existing_licence_vehicle = [v for v in self.vehicles if v.license_plate_number == license_plate_number][0]
            return f"{license_plate_number} belongs to another vehicle."
        except IndexError:
            vehicle = self.VALID_VEHICLE_TYPES[vehicle_type](brand, model, license_plate_number)
            self.vehicles.append(vehicle)
            return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        longer_route = [r for r in self.routes if r.start_point == start_point and r.end_point == end_point and
                        r.length > length]
        if longer_route:
            longer_route[0].is_locked = True

        routes = [r for r in self.routes if r.start_point == start_point and
                 r.end_point == end_point and r.length == length]
        if routes:
            return f"{start_point}/{end_point} - {length} km had already been added to our platform."
        routes = [r for r in self.routes if r.start_point == start_point and
                   r.end_point == end_point and r.length < length]
        if routes:
            return f"{start_point}/{end_point} shorter route had already been added to our platform."
        current_route_id = self.__define_next_route()
        new_route = Route(start_point, end_point, length, current_route_id)
        self.routes.append(new_route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str,
                  route_id: int,  is_accident_happened: bool):

        user = [u for u in self.users if u.driving_license_number == driving_license_number][0]
        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        vehicle_to_drive = [v for v in self.vehicles if v.license_plate_number == license_plate_number][0]
        if vehicle_to_drive.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        route_to_take = [r for r in self.routes if r.route_id == route_id][0]
        if route_to_take.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle_to_drive.drive(route_to_take.length)
        if is_accident_happened:
            vehicle_to_drive.is_damaged = True
            user.decrease_rating()
        else:
            user.increase_rating()

        return str(vehicle_to_drive)

    def repair_vehicles(self, count: int):
        damaged_vehicles = [v for v in self.vehicles if v.is_damaged]
        damaged_vehicles = sorted(damaged_vehicles, key=lambda v: (v.brand, v.model))
        if len(damaged_vehicles) > count:
            damaged_vehicles = damaged_vehicles[:count]

        for auto in damaged_vehicles:
            auto.recharge()
            auto.is_damaged = False
        return f"{len(damaged_vehicles)} vehicles were successfully repaired!"

    def users_report(self):
        result = "*** E-Drive-Rent ***\n"
        sorted_users = sorted(self.users, key=lambda u: -u.rating)
        result += '\n'.join([str(u) for u in sorted_users])
        return result
