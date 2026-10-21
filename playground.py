from src.refuge.exceptions import ValidationError, MissionRefusedError
from src.refuge.models.species import Dragon, Phoenix, Unicorn, Griffin
from src.refuge.models.creature import Creature
from src.refuge.models.mixins import FlyingMixin

class RoboticGuard:
    def __init__(self, name: str, model: str) -> None:
        self.name = name
        self.model = model

    def special_ability(self) -> str:
        return f"{self.name} patrols the perimeter and fires laser beams."

    def mission_duration_days(self) -> int:
        return 1

    def __str__(self) -> str:
        return f"{self.name} [Robotic Guard — model {self.model}]"

def end_of_day_report(residents: list) -> None:
    for resident in residents:
        print(f"--- {resident.name} ---")
        print(resident.special_ability())
        print(f"Mission duration if sent: {resident.mission_duration_days()} days")
        print(resident)

end_of_day_report([RoboticGuard("Sentinel", "RX-7")])