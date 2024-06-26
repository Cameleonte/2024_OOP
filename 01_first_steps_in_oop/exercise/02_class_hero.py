from typing import Optional


class Hero:
    def __init__(self, name: str, health: float):
        self.name = name
        self.health = health

    def defend(self, damage: float) -> Optional[str]:
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            return f"{self.name} was defeated"

    def heal(self, amount: float) -> None:
        self.health += amount


hero = Hero("Peter", 100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))
