import pygame
from pygame.transform import scale_by, rotate
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
def prepare_grass(width, height, density=10):  # When density increases, the # of grass is actually reduced
    grass = []
    for h in range(height // density):
        for w in range(width // density):
            sprite = randint(0, 11)
            position = round(w * density + randint(4, 12), 4), round(h * density + randint(4, 12), 4)
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

# Calculating angles
angles = [35 * (cos(i / 80) - 0.4) for i in range(500)]

# Setting up all rotations of sprites
Sprites = [[scale_by(rotate(sprite, angle), (4, 4))
           for angle in angles]
           for sprite in sprites]

# Because the grass now needs to move away from the mouse pointer if it's close enough, checks need to be made.
# These checks are very costly on the performance, because the program checks for every blade of grass.
# It also needs to do the calculations we worked to avoid for the close grass blades.
# For the 500x500 window, I experienced a drop of ~10 frames, which still keeps the program at a comfy 45 fps.

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
    Xpos, Ypos = pygame.mouse.get_pos()

    # Drawing each blade of grass
    for blade in Grass:
        blade['step'] += 1 if blade['step'] < 499 else -499

        # Checking the grass blade's proximity to the mouse
        dx = blade['position'][0] - Xpos
        dy = blade['position'][1] - Ypos
        if -50 < dx < 50 and -50 < dy < 50:
            angle1 = angles[blade['step']]
            angle1 *= dy / 50  # Taking percentage of normal angle

            angle2 = 50 - dx if dx < 0 else -50 - dx
            angle2 *= 1 - abs(dy) / 50  # Taking percentage of new angle from mouse

            angle = angle1 + angle2  # Adding the two angles to get the new angle for the grass blade
            image = scale_by(rotate(sprites[blade['sprite']], angle), (4, 4))

        else:  # If it's not near the mouse pointer, load the normal image
            image = Sprites[blade['sprite']][blade['step']]

        x, y = blade['position']
        x, y = round(x - 0.5 * image.get_width(), 4), round(y - 0.5 * image.get_height(), 4)  # Centring the image

        screen.blit(image, (x, y))

    pygame.display.flip()
    clock.tick(60)
