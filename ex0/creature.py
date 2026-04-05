from abc import ABC, abstractmethod
from typing import Any


class Creature(ABC):
    def __init__(self, name: str, card_type: str, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.name = name
        self.card_type = card_type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return "Standard Message"


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass
