import pygame, sys
from game import Game
from colors import Colors

pygame.init()
# text
title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)
# rectangles for text
score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)
# creates game window
screen = pygame.display.set_mode((500, 620))
# title
pygame.display.set_caption("Python Tetris")
# controls frame rate of game
clock = pygame.time.Clock()
# starts game loop
game = Game()
# slows down the block so it does not immediately drop to the bottom
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

while True:
    for event in pygame.event.get():
        # exit sequence for quitting game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # what to do when a specific key is pressed
        if event.type == pygame.KEYDOWN:
            # press any key to reset game
            if game.game_over == True:
                game.game_over = False
                game.reset()
            # move left
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            # move right
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            # move down
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
                game.update_score(0, 1)
            # rotate block
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()
        # keeps the blocks coming during gameplay
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()

    # updates score value
    score_value_surface = title_font.render(str(game.score), True, Colors.white)
    # make screen background dark blue
    screen.fill(Colors.dark_blue)
    # set surface location for score and next block
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (375, 180, 50, 50))
    # shows GAME OVER when player loses
    if game.game_over == True:
        screen.blit(game_over_surface, (320, 450, 50, 50))

    # create rectangle for score and center the value
    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, centery = score_rect.centery))
    # create rectangle for next block
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
    # creates the screen the user interacts with
    game.draw(screen)
    # updates the screen
    pygame.display.update()
    # will run 60 times per second
    clock.tick(60)
