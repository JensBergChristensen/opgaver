import pygame

pygame.init()

screenSize = (800, 700)
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("square move")
done = False

is_blue = True
x = 650
y = 550
a = 30
b = 30

clock = pygame.time.Clock()

player1 = pygame.Rect(*screen.get_rect().center, 0, 0).inflate(75, 75)
player2 = pygame.Rect(0, 0, 75, 75)


while not done:
        for event in pygame.event.get():
                # !!! GET EVENT !!!
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    is_blue = not is_blue
        # !!! GET KEYS !!!
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3

        if pressed[pygame.K_w]: b -= 3
        if pressed[pygame.K_s]: b += 3
        if pressed[pygame.K_a]: a -= 3
        if pressed[pygame.K_d]: a += 3

        # !!! GRAPHICS !!!

        screen.fill((0, 0, 0))
        if is_blue: color = (0, 128, 255)
        else: color = (255, 100, 0)

        collide = player1.colliderect(player2)
        if collide: color = (0,255, 200)

        player1 = pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
        player2 = pygame.draw.rect(screen, color, pygame.Rect(a, b, 60, 60))

        pygame.display.flip()
        clock.tick(60)
