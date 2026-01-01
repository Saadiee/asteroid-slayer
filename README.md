# Asteroids

**A minimal, extensible Asteroids-style game built with Python and Pygame** 🎮

> Work-in-progress — a small learning project and code example for building 2D games with modern Python.

---

## Table of Contents

- [About](#about)
- [Features](#features)
- [Demo](#demo)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Controls](#controls)
- [Project Structure](#project-structure)
- [Development Notes](#development-notes)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## About

Asteroids is a compact Python implementation of the classic arcade game. It demonstrates sprite management, simple physics, and structured game loops using `pygame`. The project is intended as both a learning exercise and a small base for expansion.

---

## Features ✅

- Player-controlled ship with rotation and thrust
- Simple sprite groups for update/draw management
- Runtime logging of game state to `game_state.jsonl` and game events to `game_events.jsonl`
- Clean, modular code suitable for extension (e.g., asteroids, bullets, scoring)

---

## Demo

Add a screenshot or short GIF here to show the game in action. Replace the line below with an image when available:

![Placeholder screenshot](docs/screenshot.png)

---

## Requirements ⚙️

- Python >= 3.12
- pygame == 2.6.1

> The project uses simple, single-file modules to keep the codebase approachable.

---

## Installation

Recommended: create and use a virtual environment.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install pygame==2.6.1
```

If you plan to package or extend the project, consider using `pip` editable installs or a dependency tool that reads `pyproject.toml`.

---

## Usage

Run the game from the repository root:

```bash
python main.py
```

The game creates `game_state.jsonl` (and `game_events.jsonl`) while running — useful for debugging and snapshots of sprite state.

---

## Controls

- W: Thrust forward
- S: Reverse thrust
- A: Rotate left
- D: Rotate right
- Close the window or press the window close control to quit

---

## Project Structure 🔧

- `main.py` — application entry point and main loop
- `player.py` — player ship behavior and movement
- `circleshape.py` — base circle-shaped sprite helper
- `constants.py` — screen size and gameplay constants
- `logger.py` — lightweight state/event logger (writes `.jsonl` files)
- `game_state.jsonl` — (generated) logged game state samples
- `pyproject.toml` — project metadata and dependencies

---

## Development Notes 🛠️

- Logging runs for a limited time (`logger._MAX_SECONDS`) and samples sprites to avoid huge logs.
- The game uses `pygame.sprite.Group` to manage updatable and drawable objects.
- Consider adding automated tests, continuous integration, and packaging metadata if this project is intended for sharing.

---

## Roadmap

- [ ] Add asteroids and basic collision handling
- [ ] Add bullets / shoot mechanic
- [ ] Implement scoring and UI overlay
- [ ] Add sound effects and music
- [ ] Create automated tests and CI workflow

---

## Contributing

Contributions, issues, and feature requests are welcome! If you'd like to contribute:

1. Fork the repository
2. Create a feature branch
3. Open a pull request with a clear description of your changes

---

## License

This repository does not include a license by default.

---
