from pygame import *

#adding classes
class GameSprite(sprite.Sprite):
    def __init__(self, player_speed, player_x, player_y, player_image, w=50, h=50):
        super().__init__() 
        self.speed = player_speed
        self.image = transform.scale(image.load(player_image), (w, h))
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
        elif key_pressed_o[K_DOWN] and self.rect.y <  345:
            self.rect.y += 10
    def update_l(self):
        key_pressed_t = key.get_pressed()
        if key_pressed_t[K_w] and self.rect.y > 5:
            self.rect.y -= 10
        elif key_pressed_t[K_s] and self.rect.y < 345:
            self.rect.y += 10
            
def move_ball():
    global speed_x, speed_y, finish
    
    ball.rect.x += speed_x
    ball.rect.y += speed_y
        
    if ball.rect.y <= 0 or ball.rect.y >= 450:
        speed_y *= -1
    if ball.rect.x <= 0 or ball.rect.x >= 650:
        finish = True
    if sprite.collide_rect.top(platform1, ball):
        speed_x *= -1
    if sprite.collide_rect(platform2, ball):
        speed_x *= -1
#creating a window
w, h = 700, 500
window = display.set_mode((w, h))
display.set_caption("Ping pong pix by Tok")
clock = time.Clock()
finish = False

speed_x = 5
speed_y = 5

background = transform.scale(image.load("background.png"), (w,h))


#platform
platform1 = Player(10, 50, 150, "platformd.png", 18, 125)
platform2 = Player(10, 635, 150, "platformd2.png", 18, 125)
ball = GameSprite(10, 325, 225, "ball.png", 50, 50)


#game cycle
game = 1
while game:
    window.blit(background, (0,0))
    
    for e in event.get():
        if e.type == QUIT:
            game = 0
    if finish == False:
    
        platform1.reset()#show platform1
        platform1.update_l()#move platform1
        
        platform2.reset()#show platform2
        platform2.update_r()#move platform2
        
        ball.reset() #show ball
        
        move_ball() #move ball
            
        display.update()   
        clock.tick(60)

