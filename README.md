# 🗡️ RPG - Text RPG Game

A simple text-based RPG game built with Python, refactored using Object-Oriented Programming (OOP) principles.

This project started as a procedural Python RPG and was later refactored into an object-oriented structure to improve organization, maintainability, and scalability.

## 🎮 How to play

Clone the repository and run:

```bash
python main.py
```

Follow the instructions displayed in the terminal to create your character and start playing.

## ⚔️ Features

* Choose your character class at the start of the game
* Turn-based combat system
* Different character classes
* Character attributes such as health, attack, mana, and gold
* Enemy system with different attributes
* Special attacks and abilities
* In-game shop
* Flee from battles
* Character status display

## 🧩 Project Structure

```text
RPG/
│
├── main.py
├── personagem.py
├── heroi.py
├── inimigo.py
├── batalha.py
├── loja.py
├── .gitignore
├── README.md
│
└── legacy/
    ├── jogo.py
    └── README.md
```

### 📄 Main files

* `main.py` — Responsible for starting the game and handling character creation.
* `personagem.py` — Contains the base `Personagem` class.
* `heroi.py` — Contains the `Heroi`, `Cavaleiro`, and `Mago` classes.
* `inimigo.py` — Contains the enemy class and enemy attributes.
* `batalha.py` — Handles the turn-based combat system.
* `loja.py` — Handles the in-game shop.

## 🧙 Character Classes

### ⚔️ Cavaleiro

A melee-focused character with high health and physical attack.

### 🔮 Mago

A magic-focused character that uses mana and magical attacks.

Each class has its own attributes and abilities, making the choice of character relevant to the gameplay.

## 🏗️ Object-Oriented Programming

The project was refactored from a procedural implementation into an Object-Oriented Programming structure.

Some of the OOP concepts used include:

* Classes and objects
* Inheritance
* Encapsulation
* Methods
* Constructors
* Code organization through responsibilities

The `Personagem` class works as a base class for characters, while classes such as `Heroi` and `Inimigo` extend its functionality.

The current structure can be represented as:

```text
Personagem
├── Heroi
│   ├── Cavaleiro
│   └── Mago
│
└── Inimigo
```

This structure makes it easier to add new characters, enemies, abilities, and mechanics in the future.

## 📜 Legacy Version

The original procedural version of the project is preserved in the [`legacy`](./legacy) folder.

The Legacy version was the starting point of the project and was later refactored into the current Object-Oriented Programming structure.

## 🚧 Work in Progress

This project is still under development.

Planned features include:

* New enemies and boss fights
* New dungeons to explore
* More items and equipment
* Expanded skills and abilities system
* More character classes
* Experience and level system
* Improved shop and inventory system

## 📚 Project Goals

This project is also being used as a practical exercise to improve my Python skills and learn how to structure larger applications using Object-Oriented Programming.

The main goal is to continuously improve the project while applying new programming concepts and best practices.

## 🛠️ Built with

* Python 3
