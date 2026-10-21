from src.refuge.models.creature import Creature

class Dragon(Creature):
    def __init__(self, name, origin, power_level, element, **kwargs):
        super().__init__(name, "Dragon", origin, power_level, **kwargs)
        self.element = element

    def __str__(self):
        return f"{super().__str__()} - element: {self.element}"

    def __repr__(self):
        return f"Dragon(name={self.name!r}, origin={self.origin!r}, power_level={self.power_level!r}, element={self.element!r})"

    def mission_duration_days(self):
        return 14

    def special_ability(self):
        return f"{self.name} breathes {self.element} and flies at great speed."
        
class Phoenix(Creature):
    def __init__(self, name, origin, power_level, resurrection_count = 0, **kwargs):
        super().__init__(name, "Phoenix", origin, power_level, **kwargs)
        self.resurrection_count = resurrection_count

    def mission_duration_days(self):
        return 7

    def special_ability(self):
        return f"{self.name} radiates a flame aura and rises again from its ashes."

    def resurrect(self):
        self.resurrection_count += 1
        return f"🔥 {self.name} rises from its ashes! (resurrection: {self.resurrection_count})"
        
class Unicorn(Creature):
    MIN_MISSION_POWER = 40

    def __init__(self, name, origin, power_level, **kwargs):
        super().__init__(name, "Unicorn", origin, power_level, **kwargs)

    def mission_duration_days(self):
        return 3

    def special_ability(self):
        return f"{self.name} heals its allies and gallops faster than the wind."

    def refusal_reason(self):
        return f"{self.name} is too weak for a mission (25 < {self.MIN_MISSION_POWER})"
        
class Griffin(Creature):
    def __init__(self, name, origin, power_level, **kwargs):
        super().__init__(name, "Griffin", origin, power_level, **kwargs)

    def mission_duration_days(self):
        return 10

    def special_ability(self):
        return f"{self.name} dives from the clouds with razor-sharp talons."
        
class Basilisk(Creature):
    def __init__(self, name, origin, power_level, **kwargs):
        super().__init__(name, "Basilisk", origin, power_level, **kwargs)

    def mission_duration_days(self):
        return 5

    def special_ability(self):
        return f"{self.name} petrifies its enemies with a single gaze."