#!/usr/bin/env python3
import ex0
import ex1
import ex2
from typing import List


def battle(oponents: List) -> None:
    print("[ ", end="")
    for op in oponents:
        if op == oponents[-1]:
            print(f"({op[0].create_base().name}+", end="")
            if isinstance(op[1], ex2.NormalStrategy):
                print("Normal) ", end="")
            elif isinstance(op[1], ex2.AggressiveStrategy):
                print("Aggressive) ", end="")
            elif isinstance(op[1], ex2.DefensiveStrategy):
                print("Defensive) ", end="")
        else:
            print(f"({op[0].create_base().name}+", end="")
            if isinstance(op[1], ex2.NormalStrategy):
                print("Normal), ", end="")
            elif isinstance(op[1], ex2.AggressiveStrategy):
                print("Aggressive), ", end="")
            elif isinstance(op[1], ex2.DefensiveStrategy):
                print("Defensive), ", end="")
    print("]\n*** Tournament ***")
    print(f"{len(oponents)} opponents involved")
    i = 0
    while i < len(oponents) - 1:
        j = i + 1
        while j < len(oponents):
            print("\n* Battle *")
            op1 = oponents[i][0].create_base()
            op2 = oponents[j][0].create_base()
            st1 = oponents[i][1]
            st2 = oponents[j][1]
            print(op1.describe(), "\nvs.\n", op2.describe(), sep="")
            print("now fight!")
            try:
                print(st1.act(op1))
                print(st2.act(op2))
            except ex2.InvalidCombination as e:
                print("Battle error, aborting tournament:", e, "\n")
            j += 1
        i += 1


if __name__ == "__main__":
    flame = ex0.FlameFactory()
    aqua = ex0.AquaFactory()
    healing = ex1.HealingCreatureFactory()
    transforming = ex1.TransformCreatureFactory()
    normal = ex2.NormalStrategy()
    aggressive = ex2.AggressiveStrategy()
    defensive = ex2.DefensiveStrategy()
    print("Tournament 0 (basic)")
    battle([(flame, normal), (healing, defensive)])
    print("\nTournament 1 (error)")
    battle([(flame, aggressive), (healing, defensive)])
    print("Tournament 2 (multiple)")
    battle([(aqua, normal), (healing, defensive), (transforming, aggressive)])
