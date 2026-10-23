from src.refuge.exceptions import ValidationError, MissionRefusedError
from src.refuge.models.species import Dragon, Basilisk, Phoenix, Unicorn, Griffin
from src.refuge.models.creature import Creature
from src.refuge.models.mixins import FlyingMixin
from src.refuge.models.employee import Handler, Veterinarian

aldric = Handler("Aldric Stone", "aldric@refuge.example", 5)
brynn = Handler("Brynn Ashford", "brynn@refuge.example", 3)
dara = Veterinarian("Dara Quill", "dara@refuge.example")
frostbite = Dragon("Frostbite", "Nordic Realms", 95, "ice")

for employee in (aldric, brynn, dara):
    print(employee, "|", employee.describe_duties())
print([e.full_name for e in (aldric, brynn, dara) if e.can_escort(frostbite)])
print(dara.can("perform_checkup"), brynn.can("perform_checkup"))
print(dara.perform_checkup(Basilisk("Gorgo", "Serpent Marsh", 91), "quarantine", "Unstable petrifying gaze"))

try:
    Handler("Cael Morrow", "cael@refuge.example", 7)
except ValidationError as error:
    print(error)