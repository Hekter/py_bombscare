# Things wouldn't be possible without the glorious and beautiful pygame.
import pygame
# For.. random.
import random

# Custom imports!
# Import the bombs class file for bombs.
import bombs
# Import the player class file for ... player.
import player
# Startup scripts!
import themeloader

# Define some globals.
# pygame takes RGB values for colors
WHITE = (255, 255, 255)

# Use the sprite.Group()s to group together the sprites into a fancy list.
bomb_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

# Screen width/height setting. 15 bombs across, 11 bombs "deep"
SCREEN_WIDTH = 15 * themeloader.block_size
SCREEN_HEIGHT = 11 * themeloader.block_size

# Now we divvy up the screen width in to sixteen-pixel-long pieces because that's how big the bombs are.
SCREEN_WIDTH_BLOCKS = SCREEN_WIDTH // themeloader.block_size
print(type(SCREEN_WIDTH_BLOCKS))

# Initializes the screen.
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

for i in range(5):

    # Initialize a BlackBomb class as bomb and pass it the handle to the image.
    bomb = bombs.BlackBomb(themeloader.BLACK_BOMB_IMAGE)

    # Now we are generating a random location for the bomb to "spawn" in above the board.
    # Board is divided into "blocks" set by the theme.
    bomb.rect.x = random.randrange(0, SCREEN_WIDTH_BLOCKS) * themeloader.block_size
    bomb.rect.y = random.randrange(-(themeloader.block_size * 5), 0, 16)

    # Add them to our sprite groups!
    bomb_list.add(bomb)
    all_sprites_list.add(bomb)

player_instance = player.Player(themeloader.PLAYER_IMAGE)
all_sprites_list.add(player_instance)

# Implement an FPS clock
clock = pygame.time.Clock()

# Start the player out in the middle of the screen.
player_instance.rect.x = (7 * themeloader.block_size)
player_instance.rect.y = (10 * themeloader.block_size)

# WE'RE NOT DONE YET
done = False

while done == False:

    # Event handling. WOO.
    for event in pygame.event.get():

        # TIL that you have to handle when Windows asks you to friggin' close.
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -16
            if event.key == pygame.K_RIGHT:
                x_speed = 16
            if event.key == pygame.K_UP:
                y_speed = -16
            if event.key == pygame.K_DOWN:
                y_speed = 16

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_speed = 0
            if event.key == pygame.K_RIGHT:
                x_speed = 0
            if event.key == pygame.K_UP:
                y_speed = 0
            if event.key == pygame.K_DOWN:
                y_speed = 0
            if event.key == pygame.K_ESCAPE:
                done = True

    # Start game logic.
    bomb_list.update()

    # This runs the spritecollide() function inside pygame to figure out if we've hit a bomb! Easy peasy.
    # Returns a list of collided sprites. In this case, that we've hit a bomb.
    bomb_hit = pygame.sprite.spritecollide(player_instance, bomb_list, False)

    # If there is a bomb on the list that we hit, do a quick check to see if we explode (black bomb).
    for bomb in bomb_hit:
        if bomb.does_explode == True:
            print("GAME OVER, YOU LOSE!")
            done = True

    # Drawing commands!
    screen.fill(WHITE)
    # Draw every sprite on the screen!
    all_sprites_list.draw(screen)

    # Do a "tick" forward in time, up to sixty times in a second.
    clock.tick(60)

    # Flip the display over so that it can be seen by the player.
    pygame.display.flip()

pygame.quit()