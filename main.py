from pygame import *
from random import randint
init()

DISPLAY_SIZE = (600, 500)
FPS = 60

mixer.init()
mixer.music.load("Background_music.ogg")
mixer.music.play()

window = display.set_mode(DISPLAY_SIZE)
display.set_caption("Shooter")
clock = time.Clock()

score = 0
goal = 10
lost = 0
max_lost = 3
life = 3

class GameSprite(sprite.Sprite):
    def __init__(self, file_image, x, y, speed):
        super().__init__()
        self.image = transform.scale(image.load(file_image), (70, 70))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < DISPLAY_SIZE[0] - self.rect.width:
            self.rect.x += self.speed

    def fire(self):
        bullet = Bullet("Micro.png", self.rect.centerx, self.rect.top, 15)
        bullets.add(bullet)

class Enemy(GameSprite):
    def update(self):
       self.rect.y += self.speed
       global lost
       if self.rect.y > DISPLAY_SIZE[1]:
           self.rect.x = randint(80, DISPLAY_SIZE[0] - 80)
           self.rect.y = 0
           lost = lost + 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()
        

enemies = sprite.Group()
for i in range(1, 6):
    enemy = Enemy("Enemy_images.png", randint(80, DISPLAY_SIZE[0] - 80), -40, randint(1, 5))
    enemies.add(enemy)
bullets = sprite.Group()

background = transform.scale(image.load("Forest.jpg"), DISPLAY_SIZE)
player = Player("Player_images.png", (DISPLAY_SIZE[0] - 70) / 2, DISPLAY_SIZE[1] - 70, 5)
#enemy = Enemy("Enemy_images.png", (DISPLAY_SIZE[0] - 70) / 2, DISPLAY_SIZE[1] - 700, 3)

start = True
while start:
    for e in event.get():
        if e.type == QUIT:
            start = False
        if e.type == KEYDOWN:
            if e.key == K_e:
                player.fire()
        
    window.blit(background, (0, 0))
    player.draw()
    player.update()
    enemies.draw(window)
    enemies.update()

    bullets.update()
    bullets.draw(window)

    display.update()
    clock.tick(FPS)