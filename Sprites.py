import pygame
from Settings import *
import math
class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        # initialise sprite attributes
        self.group = game.entities
        pygame.sprite.Sprite.__init__(self, self.group)
        self.game = game
        self.image_load = pygame.image.load(GAME_PLAYER).convert_alpha()
        self.x = x * T_SIZE
        self.y = y * T_SIZE
        self.vx = 0
        self.vy = 0
        self.rotation = 0
        self.rect = self.image_load.get_rect(center = (self.x, self.y))


    # set speed functionality (0.7071 since 1/sqrt2 pythag. theorem for diagonal movement)
    def velocity(self):
        self.vx, self.vy = 0, 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.vx = -PLAYER_SPEED
            self.rotation = 90
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.vx = PLAYER_SPEED
            self.rotation = -90
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.vy = -PLAYER_SPEED
            self.rotation = 0
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.vy = PLAYER_SPEED
            self.rotation = 180
        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071

    # update player pos according to speed
    def update(self):
        self.velocity()
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.image = pygame.transform.rotate(self.image_load, self.rotation)
        self.rect.x = self.x
        self.collide_with_walls('x')
        self.rect.y = self.y
        self.collide_with_walls('y')

    # make sure that movement in the direction of a wall is prevented
    def collide_with_walls(self, direction):
        if direction == 'x':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
        if direction == 'y':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y


class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        # initialise wall attributes
        self.group = game.entities, game.walls
        pygame.sprite.Sprite.__init__(self, self.group)
        self.game = game
        self.image = pygame.Surface((32, 32))
        self.image.fill("GREEN")
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * 32
        self.rect.y = y * 32

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.group = game.enemies
        pygame.sprite.Sprite.__init__(self, self.group)
        self.game = game
        self.image = pygame.Surface((32, 32))
        self.image.fill("BLUE")
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * 32
        self.rect.y = y * 32
        




    



