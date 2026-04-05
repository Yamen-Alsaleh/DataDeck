# DataDeck — Abstract Card Architecture

> *"Gotta catch 'em all; but sometimes, the real treasure is the skills we made along the way."*

A Python project built at **42** that explores advanced object-oriented design patterns through a creature-based card game system. By the end of this project, you'll think like a senior architect — designing systems that are modular, extensible, and clean.

---

## Table of Contents

- [Overview](#overview)
- [Design Patterns](#design-patterns)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Usage](#usage)
- [Exercises](#exercises)
- [Author](#author)

---

## Overview

DataDeck is a modular card system where creatures are dynamic data entities grouped into families with unique capabilities and battle strategies. The project is structured around three progressive exercises, each introducing a new layer of abstraction on top of the previous one.

---

## Design Patterns

| Pattern | Exercise | Description |
|---|---|---|
| **Abstract Factory** | ex0 | Create creature families (Flame, Aqua) without exposing concrete classes |
| **Interface / Mixin** | ex1 | Add independent capabilities (Heal, Transform) via multiple inheritance |
| **Strategy** | ex2 | Decouple battle behavior (Normal, Aggressive, Defensive) from creature logic |

---

## Project Structure

```
DataDeck/
│
├── ex0/                    # Abstract Factory — Creature families
│   └── __init__.py         # Exposes factories only (no concrete classes)
│
├── ex1/                    # Capabilities — Heal & Transform mixins
│   └── __init__.py         # Exposes factories only
│
├── ex2/                    # Abstract Strategy — Battle strategies
│   └── __init__.py
│
├── battle.py               # Tests ex0: factory creation & creature battles
├── capacitor.py            # Tests ex1: healing & transforming creatures
└── tournament.py           # Tests ex2: full multi-creature tournament
```

---

## Requirements

- Python **3.10** or later
- No external libraries (standard library only)
- Code must comply with **flake8** style standards
- All code must have complete **type annotations** (verified with `mypy`)
- `eval()` and `exec()` are forbidden
- Each exercise folder **must** contain a `__init__.py`

---

## Usage

Run each exercise's test script from the root of the repository:

```bash
# Exercise 0 — Creature Factory
python3 battle.py

# Exercise 1 — Capabilities
python3 capacitor.py

# Exercise 2 — Tournament
python3 tournament.py
```

---

## Exercises

### Exercise 0 — Creature Factory

Implements the **Abstract Factory** pattern to create creature families.

- `Creature` abstract class with `attack()` and `describe()` methods
- Concrete creatures: `Flameling`, `Pyrodon` (Fire family) and `Aquabub`, `Torragon` (Water family)
- `CreatureFactory` abstract class with `create_base()` and `create_evolved()` methods
- Concrete factories: `FlameFactory` and `AquaFactory`
- The `ex0` package exposes **factories only** — concrete creatures are never directly accessible

```
Flameling is a Fire type Creature
Flameling uses Ember!
...
Flameling uses Ember!
Aquabub uses Water Gun!
```

---

### Exercise 1 — Capabilities

Extends ex0 by adding **capability mixins** that are fully independent of the `Creature` base class.

- `HealCapability` abstract class → `heal()` method
- `TransformCapability` abstract class → `transform()` and `revert()` methods (with persistent state that affects `attack()`)
- Healing family: `Sproutling` + `Bloomelle` via `HealingCreatureFactory`
- Transforming family: `Shiftling` + `Morphagon` via `TransformCreatureFactory`

```
Shiftling shifts into a sharper form!
Shiftling performs a boosted strike!
Shiftling returns to normal.
```

---

### Exercise 2 — Abstract Strategy

Introduces the **Strategy** pattern so battle logic is decoupled from creatures.

- `BattleStrategy` abstract class with `act()` and `is_valid()` methods
- `NormalStrategy` — any creature, attacks directly
- `AggressiveStrategy` — transform-capable creatures only: transform → attack → revert
- `DefensiveStrategy` — heal-capable creatures only: attack → heal
- Invalid strategy/creature combinations raise a dedicated exception
- A single `battle()` function drives a full round-robin tournament

```
Battle error, aborting tournament: Invalid Creature 'Flameling' for this aggressive strategy
```

---

## Author

| Login | School |
|---|---|
| your_login | 42 |


