from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAX_THOROUGHBRED_SPEED = 140

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    @property
    def _max_breed_speed(self):
        return self.MAX_THOROUGHBRED_SPEED

    def train(self):
        if self.speed <= 137:
            self.speed += 3
        elif self.speed > self.MAX_THOROUGHBRED_SPEED:
            self.speed = self.MAX_THOROUGHBRED_SPEED
