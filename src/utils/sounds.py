import sys
import os
import random

import pygame


class Sounds:
    die: pygame.mixer.Sound
    hit: pygame.mixer.Sound
    point: pygame.mixer.Sound
    swoosh: pygame.mixer.Sound
    wing: pygame.mixer.Sound
    background: pygame.mixer.Sound

    def __init__(self) -> None:
        if "win" in sys.platform:
            ext = "wav"
        else:
            ext = "ogg"

        # load common sounds (prefer platform extension)
        self.hit = pygame.mixer.Sound(f"assets/audio/mac-quack.{ext}")
        self.point = pygame.mixer.Sound(f"assets/audio/point.{ext}")
        self.swoosh = pygame.mixer.Sound(f"assets/audio/swoosh.{ext}")
        self.wing = pygame.mixer.Sound(f"assets/audio/anime.{ext}")
        self.background = pygame.mixer.Sound(f"assets/audio/background_theme.{ext}")

        # load multiple die songs (prefer explicit files if present)
        die_candidates = [
            "assets/audio/out.wav",
            "assets/audio/koun-hai-re_8ep4nAR.wav",
            "assets/audio/koun_hai.mp3",
            "assets/audio/tejasvi.wav",
        ]
        self.die_sounds = []
        for p in die_candidates:
            if os.path.exists(p):
                try:
                    self.die_sounds.append(pygame.mixer.Sound(p))
                except Exception:
                    # ignore files that fail to load
                    pass

        # fallback: try the original die.<ext> style path if no candidates loaded
        if not self.die_sounds:
            try:
                self.die = pygame.mixer.Sound(f"assets/audio/out.{ext}")
            except Exception:
                self.die = None
        else:
            # keep convenience attribute for single die (first one)
            self.die = self.die_sounds[0]
        # load rom-rom song (use the wav file if present)
        rom_path_wav = "assets/audio/rom-rom.wav"
        rom_path_ogg = "assets/audio/rom-rom.ogg"
        if os.path.exists(rom_path_wav):
            self.romrom = pygame.mixer.Sound(rom_path_wav)
        elif os.path.exists(rom_path_ogg):
            self.romrom = pygame.mixer.Sound(rom_path_ogg)
        else:
            # fallback to None if not present
            self.romrom = None

    def play_die(self) -> None:
        """Play a random die sound from the loaded die_sounds list (safe)."""
        try:
            if getattr(self, "die_sounds", None):
                random.choice(self.die_sounds).play()
            elif getattr(self, "die", None):
                self.die.play()
        except Exception:
            # ignore playback errors
            pass
