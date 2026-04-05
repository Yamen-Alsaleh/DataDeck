from abc import ABC, abstractmethod
from typing import Union, Any
from ex0.creature import Creature
from ex1.capability import TransformCapability, HealCapability
from ex1.capability_factory import (Sproutling, Bloomelle, Shiftling,
                                    Morphagon)


class InvalidCombination(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, monster: Any) -> str:
        pass

    @abstractmethod
    def is_valid(self, monster: Any) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def act(self, monster: Creature) -> str:
        if self.is_valid(monster):
            return monster.attack()
        else:
            text = (f"Invalid Creature ’{monster.name}’"
                    " for this normal strategy")
            raise InvalidCombination(text)

    def is_valid(self, monster: Creature) -> bool:
        if isinstance(monster, Creature):
            return True
        return False


class AggressiveStrategy(BattleStrategy):
    def act(self, monster: Union[Shiftling, Morphagon]) -> str:
        if not self.is_valid(monster):
            text = (f"Invalid Creature ’{monster.name}’"
                    " for this aggressive strategy")
            raise InvalidCombination(text)
        else:
            text1 = monster.transform()
            text2 = monster.attack()
            text3 = monster.revert()
            return text1 + "\n" + text2 + "\n" + text3

    def is_valid(self, monster: Creature) -> bool:
        if isinstance(monster, TransformCapability):
            return True
        return False


class DefensiveStrategy(BattleStrategy):
    def act(self, monster: Union[Sproutling, Bloomelle]) -> str:
        if self.is_valid(monster):
            text1 = monster.attack()
            text2 = monster.heal()
            return text1 + "\n" + text2
        else:
            text = (f"Invalid Creature ’{monster.name}’"
                    " for this defensive strategy")
            raise InvalidCombination(text)

    def is_valid(self, monster: Creature) -> bool:
        if isinstance(monster, HealCapability):
            return True
        return False
