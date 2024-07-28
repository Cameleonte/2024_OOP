from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):
    INITIAL_STRENGTH: float = 200
    MIN_STRENGTH_TO_CLIMB: float = 100

    def __init__(self, name: str):
        super().__init__(name, ArcticClimber.INITIAL_STRENGTH)

    def can_climb(self) -> bool:
        return self.strength >= ArcticClimber.MIN_STRENGTH_TO_CLIMB

    def climb(self, peak: BasePeak) -> None:
        value_to_reduce: float = 20
        if peak.difficulty_level == "Extreme":
            self.strength -= value_to_reduce * 2
        else:
            self.strength -= value_to_reduce * 1.5

        self.conquered_peaks.append(peak.name)
