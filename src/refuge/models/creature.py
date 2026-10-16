class Creature:
    _total_creatures = 0
    VALID_SPECIES = ("Dragon", "Phoenix", "Unicorn", "Griffin", "Basilisk")

    def __init__(self, name, species, origin, power_level):
        if not Creature.is_valid_species(species):
            raise ValueError(f"Unknown species: {species}.")

        self.name = name
        self.species = species
        self.origin = origin
        self.power_level = power_level

        Creature._total_creatures += 1
        self._in_refuge = True

    def send_on_mission(self):
        self._in_refuge = False

    def return_to_refuge(self):
        self._in_refuge = True

    def __str__(self):
        return f"{self.name} the {self.species} (origin: {self.origin}) [{"in refuge" if self._in_refuge else "on mission"}]"

    @staticmethod
    def is_valid_species(species: str) -> bool:
        return species in Creature.VALID_SPECIES