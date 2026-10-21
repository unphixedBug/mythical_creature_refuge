from src.refuge.exceptions import ValidationError, MissionRefusedError
from src.refuge.models.species import Dragon, Phoenix, Unicorn, Griffin
from src.refuge.models.creature import Creature
from src.refuge.models.mixins import FlyingMixin

row = {"id": 1, "name": "Frostbite", "species": "Dragon", "origin": "Nordic Realms", "power_level": 95}

class WrongOrderDragon(Creature, FlyingMixin):
    """Même chose que Dragon, mais avec l'ordre des parents inversé."""

    def mission_duration_days(self) -> int:
        return 14

    def special_ability(self) -> str:
        return "..."

frostbite = Dragon("Frostbite", "Nordic Realms", 95, "ice")
print([cls.__name__ for cls in Dragon.__mro__])
print(frostbite.travel_mode())
print(frostbite.fly("Frozen Peaks"))
print(frostbite.flight_log)
print(Unicorn("Moonbeam", "Crystal Lake", 67).travel_mode())

print([cls.__name__ for cls in WrongOrderDragon.__mro__])
print(WrongOrderDragon("Test", "Dragon", "Lab", 10).travel_mode())

print(isinstance(frostbite, Creature), isinstance(frostbite, FlyingMixin),
      issubclass(Unicorn, FlyingMixin), issubclass(Phoenix, Dragon))