import random
from typing import List, Tuple

import pygame

from .constants import BACKGROUNDS, PIPES, PLAYERS


class Images:
    numbers: List[pygame.Surface] 
    game_over: pygame.Surface
    welcome_message: pygame.Surface
    base: pygame.Surface
    background: pygame.Surface
    player: Tuple[pygame.Surface]
    pipe: Tuple[pygame.Surface]

    def __init__(self) -> None:
        self.numbers = list(
            (
                pygame.image.load(f"assets/sprites/{num}.png").convert_alpha()
                for num in range(10)
            )
        )

        # game over sprite
        self.game_over = pygame.image.load(
            "assets/sprites/gameover.png"
        ).convert_alpha()
        def make_welcome_surface() -> pygame.Surface:
            surf_w, surf_h = 220, 100
            surf = pygame.Surface((surf_w, surf_h), pygame.SRCALPHA)

            title_font = pygame.font.Font(None, 36)
            subtitle_font = pygame.font.Font(None, 22)
            tap_font = pygame.font.Font(None, 18)

            # texts
            title = "Modiji Games"
            subtitle = "Get Ready"
            tap = "Tap to Start"

            # colors and simple shadow
            text_color = (255, 255, 255)
            shadow_color = (0, 0, 0)

            # render surfaces
            title_s = title_font.render(title, True, text_color)
            title_sh = title_font.render(title, True, shadow_color)
            sub_s = subtitle_font.render(subtitle, True, text_color)
            sub_sh = subtitle_font.render(subtitle, True, shadow_color)
            tap_s = tap_font.render(tap, True, text_color)
            tap_sh = tap_font.render(tap, True, shadow_color)

            # positions (centered)
            title_x = (surf_w - title_s.get_width()) // 2
            sub_x = (surf_w - sub_s.get_width()) // 2
            tap_x = (surf_w - tap_s.get_width()) // 2

            # vertical layout
            y = 8
            surf.blit(title_sh, (title_x + 1, y + 1))
            surf.blit(title_s, (title_x, y))
            y += title_s.get_height() + 6

            surf.blit(sub_sh, (sub_x + 1, y + 1))
            surf.blit(sub_s, (sub_x, y))
            y += sub_s.get_height() + 10

            surf.blit(tap_sh, (tap_x + 1, y + 1))
            surf.blit(tap_s, (tap_x, y))

            return surf

        self.welcome_message = make_welcome_surface()
        # base (ground) sprite
        self.base = pygame.image.load("assets/sprites/base.png").convert_alpha()
        self.randomize()

    def randomize(self):
        # select random background sprites
        rand_bg = random.randint(0, len(BACKGROUNDS) - 1)
        # select random player sprites
        rand_player = random.randint(0, len(PLAYERS) - 1)
        # select random pipe sprites
        rand_pipe = random.randint(0, len(PIPES) - 1)

        self.background = pygame.image.load(BACKGROUNDS[rand_bg]).convert()
        
        # Load and resize player sprites to match original bird size (34x24 pixels)
        bird_width, bird_height = 34, 24
        loaded_player = pygame.image.load(PLAYERS[rand_player][0]).convert_alpha()
        resized_player = pygame.transform.scale(loaded_player, (bird_width, bird_height))
        self.player = (resized_player, resized_player, resized_player)
        self.pipe = (
            pygame.transform.flip(
                pygame.image.load(PIPES[rand_pipe]).convert_alpha(),
                False,
                True,
            ),
            pygame.image.load(PIPES[rand_pipe]).convert_alpha(),
        )
