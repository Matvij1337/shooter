from pygame import *
init()

DISPLAY_SIZE = (600, 500)
FPS = 60

mixer.init()
mixer.music.load("Background_music.ogg")
mixer.music.play()

window = display.set_mode(DISPLAY_SIZE)
display.set_caption("Shooter")
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, file_image, x, y, speed):
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

background = transform.scale(image.load("Forest.jpg"), DISPLAY_SIZE)
player = Player("Player_images.png", (DISPLAY_SIZE[0] - 70) / 2, DISPLAY_SIZE[1] - 70, 5)

start = True
while start:
    for e in event.get():
        if e.type == QUIT:
            start = False

    window.blit(background, (0, 0))
    player.draw()
    player.update()

    display.update()
    clock.tick(FPS)