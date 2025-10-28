# Modiji Games (FlapPyBird fork)

A small Flappy Bird-like game modified as "Modiji Games" — lightweight Python / Pygame project.

This repository is a modified fork of FlapPyBird that replaces the original bird with a `modiji.png` sprite, shows a text-based welcome screen, and plays custom audio (including an intro `rom-rom.wav` and multiple die-sounds).

## Requirements

- Python 3.10+ (project includes a `env/` virtualenv you can use)
- pygame (install into your virtual environment)

## Quick start (macOS / zsh)

Activate the bundled virtualenv (if you want to use it):

```bash
source env/bin/activate
```

Install pygame if not already present in the active environment:

```bash
pip install pygame
```

Run the game:

```bash
python3 main.py
```

Controls

- Click or press Space / Up to start and to make the player flap.
- ESC quits the game.

What’s changed from the original

- Player sprite: uses `assets/sprites/modiji.png` (resized at runtime to match the original bird size).
- Welcome screen: now renders text (`Modiji Games`, `Get Ready`, `Tap to Start`) instead of the `message.png` image.
- Intro music: `assets/audio/rom-rom.wav` is played once when gameplay begins.
- Background theme: `assets/audio/background_theme.*` plays in a loop during gameplay.
- Die sounds: multiple die-track files are loaded (if present) and a random one is played on death.

Useful file references

- Game entry: `main.py`
- Game loop and sound handling: `src/flappy.py`
- Images loader and welcome surface: `src/utils/images.py` and `src/utils/constants.py`
- Sound loader and die-sound logic: `src/utils/sounds.py`
- Entities (player, pipes, floor, etc.): `src/entities/` directory

Customizing assets

- Replace the player image: `assets/sprites/modiji.png` (the code scales it to match the original bird size).
- Change welcome text: edit the welcome surface creation in `src/utils/images.py`.
- Swap or add die sounds: place files in `assets/audio/` (example candidates used by the project include `out.wav`, `koun-hai-re_8ep4nAR.wav`, `koun_hai.mp3`, `tejasvi.wav`) and the code will pick one at random.
- Intro music: `assets/audio/rom-rom.wav` (or `rom-rom.ogg` if present).

Troubleshooting

- If sounds aren't playing, ensure `pygame` is installed and the mixer initializes correctly. Check that the expected audio files exist in `assets/audio/` and that their filenames/extensions match what `src/utils/sounds.py` expects.
- If the modiji sprite looks too large/small, replace the image with an appropriately sized PNG or edit the scale in `src/utils/images.py`.

License

This project follows the original repository's license. See the `LICENSE` file in the repository root.

Enjoy Modiji Games! If you want visual tweaks, sound changes, or behavior updates, tell me what to change and I can update the code for you.