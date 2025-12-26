import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

pygame.init()
clock = pygame.time.Clock()
dt = 0


def main():
    print("Starting Asteroids with pygame version:", pygame.version.ver)
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()                                                               # hold all the objects that can be updated
    drawable = pygame.sprite.Group()                                                                # hold all the objects that can be drawn
    Player.containers = (updatable, drawable)                                                       # Add the Player class to the updatable and drawable groups
    player = Player(x, y)                                                                           # instanciate a player object

    while True:                                                                                     # starts game loop
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        delta_time = clock.tick(60)
        dt = delta_time / 1000
        screen.fill("black")
        updatable.update(dt)                                                                        # update all the objects
        for obj in drawable:
            obj.draw(screen)                                                                        # draw the player on screen
        pygame.display.flip()

if __name__ == "__main__":
    main()

# source .venv/bin/activate
# run command: uv run main.py
