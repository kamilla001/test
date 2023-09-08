import pygame
import random
pygame.init()
window = pygame.display.set_mode((500, 500))

background = pygame.image.load('galaxy.jpg')
background = pygame.transform.scale(background, (500, 500))
window.blit(background, (0, 0))
clock = pygame.time.Clock()

pygame.mixer.init()
pygame.mixer.music.load('space.ogg')
pygame.mixer.music.set_volume(0.3)
# pygame.mixer.music.play()

fire = pygame.mixer.Sound('fire.ogg')
fire.set_volume(0.3)



class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image), (w, h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            hero.rect.x -= self.speed
        if keys[pygame.K_d]:
            hero.rect.x += self.speed

class Enemy (GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= 500:
            self.rect.y = -50
            self.rect.x = random.randint(50,450)

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()


hero = Player('rocket.png', 220, 400, 5, 80, 100)

ufos = pygame.sprite.Group()
bullets = pygame.sprite.Group()
for i in range(5):
    enemy1 = Enemy('ufo.png', random.randint(50, 450), random.randint(-250,-50), random.randint(1,5), 80, 50)
    ufos.add(enemy1)


btn_solo = GameSprite('btn_solo.png', 200, 200, 0, 100, 50)
btn_duo = GameSprite('btn_duo.png', 175, 300, 0, 150, 50)
game = True
screen = 'menu'
while game:
    window.blit(background, (0, 0))
    if screen == 'menu':
        btn_solo.reset()
        btn_duo.reset()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            pygame.display.update()

    if screen == 'main':
        ufos.draw(window)
        ufos.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet1 = Bullet('bullet.png', hero.rect.centerx, hero.rect.y, 15, 15, 20)
                    bullets.add(bullet1)
                    fire.play()
        if pygame.sprite.groupcollide(bullets, ufos, True,True):
            enemy1 = Enemy('ufo.png', random.randint(0,450), random.randint(-250, -50), random.randint(1,6), 80, 50)
            ufos.add(enemy1)




        hero.reset()
        hero.update()

        bullets.draw(window)
        bullets.update()
        enemy1.reset()
        enemy1.update()

        pygame.display.update()
        clock.tick(60)
