class Player:

    def __init__(self, name: str, hp: int, mp: int) -> None:
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: dict = dict()
        self.guild: str = 'Unaffiliated'

    def add_skill(self, skill_name: str, mana_cost: int) -> str:
        if skill_name in self.skills:
            return "Skill already added"
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self) -> str:
        stamp = (f"Name: {self.name}" + '\n' + f"Guild: {self.guild}" +
                 '\n' + f"HP: {self.hp}" + '\n' + f"MP: {self.mp}")
        if len(self.skills) > 0:
            stamp += '\n===' + '\n==='.join([f'{skill_name} - {skill_mana_cost}'
                                            for skill_name, skill_mana_cost in self.skills.items()]) + '\n'
        else:
            stamp += '\n'
        return stamp
