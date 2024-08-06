from typing import List

from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:

    HORSE_VALID_BREEDS = {
        "Appaloosa": Appaloosa,
        "Thoroughbred": Thoroughbred
    }

    def __init__(self):
        self.horses: List[Horse] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if self.HORSE_VALID_BREEDS.get(horse_type):
            try:
                next(filter(lambda h: h.name == horse_name, self.horses))
                raise Exception(f"Horse {horse_name} has been already added!")
            except StopIteration:
                new_horse = self.HORSE_VALID_BREEDS[horse_type](horse_name, horse_speed)
                self.horses.append(new_horse)
                return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if jockey_name in [jockey.name for jockey in self.jockeys]:
            raise Exception(f"Jockey {jockey_name} has been already added!")
        new_jockey = Jockey(jockey_name, age)
        self.jockeys.append(new_jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        try:
            next(r for r in self.horse_races if r.race_type == race_type)
            raise Exception(f"Race {race_type} has been already created!")
        except StopIteration:
            new_race = HorseRace(race_type)
            self.horse_races.append(new_race)
            return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self._get_jockey(jockey_name)
        horse = self._get_horse(horse_type)
        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."
        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        jockey = self._get_jockey(jockey_name)
        race = next(filter(lambda r: r.race_type == race_type, self.horse_races), None)
        if race is None:
            raise f"Race {race_type} could not be found!"

        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."
        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = next(filter(lambda r: r.race_type == race_type, self.horse_races), None)
        if race is None:
            return f"Race {race_type} could not be found!"

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner = sorted(race.jockeys, key=lambda j: -j.horse.speed)[0]
        return (f"The winner of the {race_type} race, with a speed of {winner.horse.speed}km/h is "
                f"{winner.name}! Winner's horse: {winner.horse.name}.")

    def _get_jockey(self, jockey_name: str):
        try:
            jockey = next(filter(lambda j: j.name == jockey_name, self.jockeys), None)
        except StopIteration:
            raise f"Jockey {jockey_name} could not be found!"
        return jockey

    def _get_horse(self, horse_type: str):
        horse = next(
            filter(lambda h: (h.__class__.__name__ == horse_type and not h.is_taken), reversed(self.horses)), None)
        if not horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")
        return horse
