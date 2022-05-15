from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_speed, player_x, player_y, player_image, w=65, h=65):
        super().__init__() 
        self.speed = player_speed
        self.image = transform.scale(image.load(player_image), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        key_pressed_o = key.get_pressed()
        if key_pressed_o[K_UP] and self.rect.y < 430:
            self.rect.y += 10
        elif key_pressed_o[K_DOWN] and self.rect.y > 10:
            self.rect.y -= 10
    def update_r(self):
        key_pressed_t = ket.get_pressed()
        if key_pressed_t[K_UP] and self.rect.y < 430:
            self.rect.y += 10
        elif key_pressed_t[K_DOWN] and self.rect.y > 10:
            self.rect.y -= 10

class Enemy(GameSprite):
    def update(self):
        global missed
        self.rect.y += self.speed
        if self.rect.y >= 500:
            missed = missed + 1
            self.rect.y = 0
            self.rect.x = randint(0, 650)      

w, h = 700, 500
window = display.set_mode((w, h))
display.set_caption("Ping pong game")
clock = time.Clock()
window.fill((217,167,38))

ball = transform.scale(image.load("ball.png"), (50, 47))

game = 1 
while game:
    window.blit(ball, (100, 100))
    for e in event.get():
        if e.type == QUIT:
            game = 0
    
    display.update()
    clock.tick(60)
