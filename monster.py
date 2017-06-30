import pygame

def main():
    #setting values for window
    width = 510
    height = 480
    background_color = (0)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()
    background_image = pygame.image.load('images/background.png').convert_alpha()
    monster_image = pygame.image.load('images/monster.png').convert_alpha() 
    hero_image = pygame.image.load('images/hero.png').convert_alpha()
    goblin_image = pygame.image.load('images/goblin.png').convert_alpha() 
    monster_x = 0
    monster_y = 0
    hero_x = 50
    hero_y = 50
    goblin_x = 100
    goblin_y = 100

    # Game initialization
    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling
            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic
        monster_x = (monster_x + 5)
        if monster_x > 500: #checking to see if monster x coordinate is greater whan window width...
            monster_x == 0 #...if so, resetting to zero

            

        # Draw background
        screen.fill(background_color)

        # Game display
        screen.blit(background_image, (0, 0)) #background image
        screen.blit(monster_image, (monster_x, monster_y))
        screen.blit(hero_image, (hero_x, hero_y))
        screen.blit(goblin_image, (goblin_x, goblin_y))
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
 
if __name__ == '__main__':
    main()
