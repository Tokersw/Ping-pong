from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_speed, player_x, player_y, player_image):
        super().__init__() 
        self.speed = player_speed
        self.image = transform.scale(image.load(player_image), (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        key_pressed_o = key.get_pressed()
        if key_pressed_o[K_UP] and self.rect.y > 5:
            self.rect.y -= 10
        elif key_pressed_o[K_DOWN] and self.rect.y <  405:
            self.rect.y += 10
    def update_l(self):
        key_pressed_t = key.get_pressed()
        if key_pressed_t[K_w] and self.rect.y > 5:
            self.rect.y -= 10
        elif key_pressed_t[K_s] and self.rect.y < 405:
            self.rect.y += 10

class ball(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= 500:
            missed = missed + 1
            self.rect.y = 0
            self.rect.x = randint(0, 650)      

w, h = 700, 500
window = display.set_mode((w, h))
display.set_caption("Ping pong game")
clock = time.Clock()

ball = transform.scale(image.load("ball.png"), (50, 47))
background = transform.scale(image.load("background.png"), (w, h))

platform1 = Player(10, 1, 5, "platform1.png")
platform2 = Player(10, 629, 330, "platform2.png")

game = 1 
while game:
    window.blit(ball, (100, 100))
    window.blit(background, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = 0
    
    platform1.reset()
    platform1.update_l()

    platform2.reset()
    platform2.update_r()

    display.update()
    clock.tick(60)
