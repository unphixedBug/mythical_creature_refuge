from src.refuge.exceptions import ValidationError, MissionRefusedError
from abc import ABC, abstractmethod

class Creature(ABC):
    _total_creatures = 0
    VALID_SPECIES = ("Dragon", "Phoenix", "Unicorn", "Griffin", "Basilisk")

    def __init__(self, name, species, origin, power_level):
        if not Creature.is_valid_species(species):
            raise ValidationError(f"Unknown species: {species!r}.")

        self.name = name
        self.species = species
        self.__origin = origin
        self.power_level = power_level
        self._in_refuge = True

        Creature._total_creatures += 1

    def send_on_mission(self):
        '''
        Raises MissionRefusedError when the creature cannot leave.
        '''
        if not self._in_refuge:
            raise MissionRefusedError(f"{self.name} is already on a mission.")

        reason = self.refusal_reason()     

        if reason != None:
            raise MissionRefusedError(reason)
        
        self._in_refuge = False
        
    def refusal_reason(self):
        '''
        Later
        '''
        return None

    def return_to_refuge(self):
        self._in_refuge = True

    def __str__(self):
        return f"{self.name} the {self.species} (origin: {self.origin}) [{"in refuge" if self._in_refuge else "on mission"}]"

    @staticmethod
    def is_valid_species(species: str) -> bool:
        return species in Creature.VALID_SPECIES

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["species"], data["origin"], data["power_level"])

    @classmethod
    def from_string(cls, text):
        attr = text.split(", ")

        if len(attr) != 4:
            raise ValidationError(f"Got {len(attr)} informations instead of 4")

        name, species, origin, power_level = attr

        return cls(name, species, origin, int(power_level))

    @classmethod
    def get_total_creatures(cls):
        return cls._total_creatures

    @property
    def power_level(self):
        return self._power_level

    @power_level.setter
    def power_level(self, value):
        if not isinstance(value, int) or isinstance(value, bool):
            raise ValidationError(f"Must be an int, got {type(value).__name__}")
        if value < 0 or value > 100:
            raise ValidationError(f"Must be between 0 and 100, got {value}")

        self._power_level = value

    @property
    def origin(self):
        return self.__origin

    @property
    def in_refuge(self):
        return self._in_refuge

    def __repr__(self):
        return f"Creature(name={self.name!r}, species={self.species!r}, origin={self.origin!r}, power_level={self.power_level!r})"

    @abstractmethod
    def mission_duration_days():
        '''
        Subclass
        '''

    @abstractmethod
    def special_ability():
        '''
        Subclass
        '''