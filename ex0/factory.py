from .creature import Creature, CreatureFactory, Any


class Charmander(Creature):
    def __init__(self, **kwargs: Any):
        super().__init__("Charmander", "Fire", **kwargs)

    def attack(self) -> str:
        return "Charmander uses Ember!"

    def describe(self) -> str:
        return f"Charmander is a {self.card_type} type Creature"


class Charzard(Creature):
    def __init__(self, **kwargs: Any):
        super().__init__("Charzard", "Fire/Flying", **kwargs)

    def attack(self) -> str:
        return "Charzard uses Flamethrower!"

    def describe(self) -> str:
        return f"Charzard is a {self.card_type} type Creature"


class Squirtle(Creature):
    def __init__(self, **kwargs: Any):
        super().__init__("Squirtle", "Water", **kwargs)

    def attack(self) -> str:
        return "Squirtle uses Water Gun!"

    def describe(self) -> str:
        return f"Squirtle is a {self.card_type} type Creature"


class Blastoise(Creature):
    def __init__(self, **kwargs):
        super().__init__("Blastoise", "Water", **kwargs)

    def attack(self) -> str:
        return "Blastoise uses Hydro Pump!"

    def describe(self) -> str:
        return f"Blastoise is a {self.card_type} type Creature"


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Charmander()

    def create_evolved(self) -> Creature:
        return Charzard()


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Squirtle()

    def create_evolved(self) -> Creature:
        return Blastoise()
