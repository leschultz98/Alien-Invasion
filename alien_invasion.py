import pygame
from pygame.sprite import Group

from settings import Settings
from screen import Screen
from ship import Ship
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
import game_functions as gf


def run_game():
    """Initialize game, settings and create a screen object."""
    pygame.init()
    ai_settings = Settings()
    screen = Screen()

    # Make the Play button.
    play_button = Button(screen, "Play")

    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make a ship, a group of bullets and a group of aliens.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Start main loop for the game.
    while True:
        gf.check_event(ai_settings, screen, stats, sb, play_button, ship,
                       aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens,
                             bullets)
            gf.update_bullet(ai_settings, screen, stats, sb, ship, aliens,
                             bullets)
        gf.update_screen(screen, stats, sb, ship, aliens, bullets, play_button)


run_game()