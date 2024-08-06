from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAX_APPALOOSA_SPEED = 120

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    @property
    def _max_breed_speed(self):
        return self.MAX_APPALOOSA_SPEED

    def train(self):
        if self.speed <= 118:
            self.speed += 2
        elif self.speed > self.MAX_APPALOOSA_SPEED:
            self.speed = self.MAX_APPALOOSA_SPEED
