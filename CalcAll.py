import pygame
from random import randint
from math import cos


# Preparing method for splitting sprite sheet into correct parts
def prepare_sheet(directory, width, height):
    slices = []
    sheet = pygame.image.load(directory).convert_alpha()
    for i in range(sheet.get_width() // width):
        image = pygame.Surface((width, height + 8), pygame.SRCALPHA)
        image.blit(sheet, (0, 0), (i * width, 0, (i + 1) * width, height))
        slices.append(image)
    return slices


# Preparing method for setting up grass, based on screen dimensions
def prepare_grass(width, height, density=10):
    grass = []
    for w in range(width // density):
        for h in range(height // density):
            sprite = randint(0, 11)
            position = w * density - randint(2, 8) + 5, h * density - randint(2, 8) + 5
            step = int(position[0] + 0.3 * position[1])
            blade = {'sprite': sprite,
                     'position': position,
                     'step': step}
            grass.append(blade)
    return grass


# Initialising game
pygame.init()

X, Y = 500, 500
screen = pygame.display.set_mode((X, Y), pygame.RESIZABLE)
clock = pygame.time.Clock()
pygame.display.set_caption('Moving Grass')

# Preparing Grass
Grass = prepare_grass(X, Y)

# Unpacking sprites
sprites = prepare_sheet('Grass.png', 5, 10)

# Main loop
while True:
    # Checking events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.VIDEORESIZE:
            X, Y = pygame.display.get_surface().get_size()
            Grass = prepare_grass(X, Y)

    screen.fill((47, 131, 39))

    # Drawing each blade of grass
    for blade in Grass:
        blade['step'] += 2
        angle = 45 * (cos(blade['step'] / 40) - 0.4)

        image = sprites[blade['sprite']]
        image = pygame.transform.rotate(image, angle)
        image = pygame.transform.scale_by(image, (4, 4))

        x, y = tuple(blade['position'])
        x, y = x - 0.5 * image.get_width(), y - 0.5 * image.get_height()

        screen.blit(image, (x, y))

    pygame.display.flip()
    clock.tick(60)
