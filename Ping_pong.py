from pygame import *

w, h = 700, 500
window = display.set_mode((w, h))
display.set_caption("Ping pong game")
clock = time.Clock()

game = 1 
while game:
    for e in event.get():
        if e.type == QUIT:
            game = 0

    window.fill((217,167,38))
    display.update()
    clock.tick(60)