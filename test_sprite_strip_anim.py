"""
This demo script aims at testing
and demonstrating 
the functions of sprite_strip_anim.py

Ref: https://www.pygame.org/wiki/Spritesheet
"""

"""
Sprite strip animator demo

Requires spritesheet.Spritesheet, sprite_strip_anim.SpriteStripAnim
and the Explode1.bmp through Explode5.bmp
found in the sprite pack at
https://lostgarden.com/2005/03/30/download-a-complete-set-of-sweet-8-bit-sinistar-clone-graphics/

I had to make the following addition to method Spritesheet.image_at in
order to provide the means to handle sprite strip cells with borders:

            elif type(colorkey) not in (pygame.Color,tuple,list):
                colorkey = image.get_at((colorkey,colorkey))
"""
import sys
import pygame
from pygame.locals import Color, KEYUP, K_ESCAPE, K_RETURN
from sprite_strip_anim import SpriteStripAnim

surface = pygame.display.set_mode((100,100))
FPS = 120
frames = FPS / 12
folder_prefix = 'test_images/'
strips = [
    SpriteStripAnim(folder_prefix + 'Explode1.bmp', (0,0,24,24), 8, 1, True, frames),
    SpriteStripAnim(folder_prefix + 'Explode2.bmp', (0,0,12,12), 7, 1, True, frames),
    SpriteStripAnim(folder_prefix + 'Explode3.bmp', (0,0,48,48), 4, 1, True, frames) +
    SpriteStripAnim(folder_prefix + 'Explode3.bmp', (0,48,48,48), 4, 1, True, frames),
    SpriteStripAnim(folder_prefix + 'Explode4.bmp', (0,0,24,24), 6, 1, True, frames),
    SpriteStripAnim(folder_prefix + 'Explode5.bmp', (0,0,48,48), 4, 1, True, frames) +
    SpriteStripAnim(folder_prefix + 'Explode5.bmp', (0,48,48,48), 4, 1, True, frames)
]
black = Color('black')
clock = pygame.time.Clock()
n = 0
strips[n].iter()
image = strips[n].next()
while True:
    for e in pygame.event.get():
        if e.type == KEYUP:
            if e.key == K_ESCAPE:
                sys.exit()
            elif e.key == K_RETURN:
                n += 1
                if n >= len(strips):
                    n = 0
                strips[n].iter()
    surface.fill(black)
    surface.blit(image, (0,0))
    pygame.display.flip()
    image = strips[n].next()
    clock.tick(FPS)