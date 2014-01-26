mmx-legacy-info
===============

Information parser and reusable web api for the game "Might and Magic X Legacy"

Overview
--------

This project tries to extract game information from the data files provided with game installation. These are mainly XML- and CSV-Files used by the Unity-Engine as streaming assets.

Requirements
------------

- python >= 3
- a copy of the game, more info here: http://might-and-magic.ubi.com/mightandmagicx-legacy
- mongodb (optional but recommended) to avoid repeated parsing and disk access

Progress and planned features
-----------------------------

### Features

- NPC dialog trees
- Map extraction
- Item information

### Technology

- Independant backend
- REST API
