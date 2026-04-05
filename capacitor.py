#!/usr/bin/env python3
import ex1


if __name__ == "__main__":
    print("Testing Creature with healing capability")
    heal_factory = ex1.HealingCreatureFactory()
    heal_base = heal_factory.create_base()
    heal_ev = heal_factory.create_evolved()
    print("base:")
    print(heal_base.describe())
    print(heal_base.attack())
    print(heal_base.heal())
    print("evolved:")
    print(heal_ev.describe())
    print(heal_ev.attack())
    print(heal_ev.heal())

    print("\nTesting Creature with transform capability")
    transform_factory = ex1.TransformCreatureFactory()
    transform_base = transform_factory.create_base()
    transform_ev = transform_factory.create_evolved()
    print("base:")
    print(transform_base.describe())
    print(transform_base.attack())
    print(transform_base.transform())
    print(transform_base.attack())
    print(transform_base.revert())
    print("evolved:")
    print(transform_ev.describe())
    print(transform_ev.attack())
    print(transform_ev.transform())
    print(transform_ev.attack())
    print(transform_ev.revert())
