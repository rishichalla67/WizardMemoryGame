import pygame, sys

pygame.init()

# Global Variables
screen = pygame.display.set_mode((1000, 750))
pygame.display.set_caption("Wizard's Knowledge Quest")
running = True
fontTitle = pygame.font.SysFont("Comic", 100)
fontSubHeader = pygame.font.SysFont(None, 60)
text = pygame.font.SysFont(None, 25)
themeColor = (204,153,255)

# Backgrounds
menuScreen_img = pygame.image.load("../../Sprites/menuBG.jpg")
menuScreen_bg = pygame.transform.scale(menuScreen_img, (1000, 750))

def draw_text(text, font, color, surface, x, y):
    textObj = font.render(text,1,color)
    textRect = textObj.get_rect()
    textRect.topleft = (x,y)
    surface.blit(textObj, textRect)
    return textRect

while running:
    screen.blit(menuScreen_bg, (0, 0))
    mx, my = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # if user wants to exit game
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # when user presses esc it leaves game
                pygame.quit()
                sys.exit()
        # if event.type == pygame.MOUSEBUTTONDOWN:
    home_button = draw_text("Wizard's Knowledge", fontTitle, themeColor, screen, 170, 125)
    home_button = draw_text("Quest", fontTitle, themeColor, screen, 400, 200)

    start_game_button = draw_text("Start Game", fontSubHeader, themeColor, screen, 75, 350)
    controls_button = draw_text("Controls", fontSubHeader, themeColor, screen, 75, 425)
    credits_button = draw_text("Credits", fontSubHeader, themeColor, screen, 75, 500)


    pygame.display.update()


