from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):
    INITIAL_STRENGTH: float = 150
    MIN_STRENGTH_TO_CLIMB: float = 75

    def __init__(self, name: str):
        super().__init__(name, SummitClimber.INITIAL_STRENGTH)

    def can_climb(self) -> bool:
        return self.strength >= SummitClimber.MIN_STRENGTH_TO_CLIMB

    def climb(self, peak: BasePeak) -> None:
        value_to_reduce: float = 30
        if peak.difficulty_level == "Advanced":
            self.strength -= value_to_reduce * 1.3
        else:
            self.strength -= value_to_reduce * 2.5

        self.conquered_peaks.append(peak.name)
