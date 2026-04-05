from ex0.creature import Creature, CreatureFactory, Any
from .capability import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    def __init__(self, **kwargs: Any):
        super().__init__("Sproutling", "Grass", **kwargs)

    def attack(self) -> str:
        return "Sproutling uses Vine Whip!"

    def describe(self) -> str:
        return f"Sproutling is a {self.card_type} type Creature"

    def heal(self) -> str:
        return "Sproutling heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self, **kwargs: Any):
        super().__init__("Bloomelle", "Grass/Fairy", **kwargs)

    def attack(self) -> str:
        return "Bloomelle uses Petal Dance!"

    def describe(self) -> str:
        return f"Bloomelle is a {self.card_type} type Creature"

    def heal(self) -> str:
        return "Bloomelle heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self, **kwargs: Any):
        super().__init__("Shiftling", "Normal", **kwargs)

    def attack(self) -> str:
        if self.attribute == 0:
            return "Shiftling attacks normally."
        else:
            return "Shiftling performs a boosted strike!"

    def describe(self) -> str:
        return f"Shiftling is a {self.card_type} type Creature"

    def transform(self) -> str:
        self.attribute = 1
        return "Shiftling shifts into a sharper form!"

    def revert(self) -> str:
        return "Shiftling returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self, **kwargs: Any):
        super().__init__("Morphagon", "Normal/Dragon", **kwargs)

    def attack(self) -> str:
        if self.attribute == 0:
            return "Morphagon attacks normally."
        else:
            return "Morphagon unleashes a devastating morph strike!"

    def describe(self) -> str:
        return f"Morphagon is a {self.card_type} type Creature"

    def transform(self) -> str:
        self.attribute = 1
        return "Morphagon morphs into a dragonic battle form!"

    def revert(self) -> str:
        return "Morphagon stabilizes its form."


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Sproutling:
        return Sproutling()

    def create_evolved(self) -> Bloomelle:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Shiftling:
        return Shiftling()

    def create_evolved(self) -> Morphagon:
        return Morphagon()
