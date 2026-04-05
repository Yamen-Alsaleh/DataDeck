#!/usr/bin/env python3
from ex0.factory import FlameFactory, AquaFactory
from ex0.creature import CreatureFactory


def factory_test(factory: CreatureFactory) -> None:
    base = factory.create_base()
    ev = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(ev.describe())
    print(ev.attack())


def battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    base1 = factory1.create_base()
    base2 = factory2.create_base()
    print(base1.describe())
    print("vs.")
    print(base2.describe())
    print("fight!")
    print(base1.attack())
    print(base2.attack())


if __name__ == "__main__":
    print("Testing factory")
    factory_test(FlameFactory())
    print("\nTesting factory")
    factory_test(AquaFactory())
    print("\nTesting battle")
    battle(FlameFactory(), AquaFactory())
