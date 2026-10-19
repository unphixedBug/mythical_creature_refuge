from src.refuge.models.creature import Creature

class Dragon(Creature):
    def __init__(name, origin, power_level, element, **kwargs):
        super().__init__(name, origin, power_level, element, **kwargs)
        
class Phoenix(Creature):
    def __init__(name, origin, power_level, element, **kwargs):
        super().__init__(name, origin, power_level, element, **kwargs)
        
class Unicorn(Creature):
    def __init__(name, origin, power_level, element, **kwargs):
        super().__init__(name, origin, power_level, element, **kwargs)
        
class Griffin(Creature):
    def __init__(name, origin, power_level, element, **kwargs):
        super().__init__(name, origin, power_level, element, **kwargs)
        
class Basilisk(Creature):
    def __init__(name, origin, power_level, element, **kwargs):
        super().__init__(name, origin, power_level, element, **kwargs)