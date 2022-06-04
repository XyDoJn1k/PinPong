from pygame import *
import random

class GameSprite():
    def __init__(self, img, x, y, width, height, speed):
        super().__init__()
        self.image = transform.scale(
            image.load(img),
            (width, height)
        )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Rocket(GameSprite):
    def __init__(self, player_img, x, y, width, height, speed):
        super().__init__(player_img, x, y, width, height, speed)

    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >= 5:
            self.rect.x -= self.step
        elif keys[K_s] and self.rect.y <= 625:
            self.rect.x += self.step
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

window = display.set_mode((700, 500))
background = GameSprite('table.jpg', 0, 0, 700, 500, 0)
rock = Rocket("rocket.png", 0, 350, 300, 400, 5)
clock = time.Clock()
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    background.reset()
    rock.update()
    rock.reset()
    display.update()
    clock.tick(60)