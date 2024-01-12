from sys import exit
from pygame import *
from Settings import *
from Sprites import *
from os import path
from TileMap import *
vector = pygame.math.Vector2
class Main:
    def __init__(self):
        # set the display and initialise pygame
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(TITLE)
        pygame.key.set_repeat(5, 20)
        self.map = Map()
        self.setup()
        self.loop()

    # loop through tiles to generate a co-ordinate based map
    def setup(self):
        self.enemies = pygame.sprite.Group()
        self.entities = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        for row, value in enumerate(self.map.data):
            for col, values in enumerate(value):
                if values == "1":
                    Wall(self, col, row)
                if values == "P":
                    self.player = Player(self, col, row)
                if values == "E":
                    self.enemy = Enemy(self, col, row)
        self.world = WorldShift(self.map.width, self.map.height)

    # set game loop and call loop specific functions
    def loop(self):
        self.running = True
        while self.running:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    # update existing groups
    def update(self):
        self.entities.update()
        self.world.update(self.player)

    # draw coordinate grid to specify each tile
    def draw_grid(self):
        for x in range(0, SCREEN_WIDTH, T_SIZE):
            pygame.draw.line(self.screen, GREEN, (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT, T_SIZE):
            pygame.draw.line(self.screen, GREEN, (0, y), (SCREEN_WIDTH, y))

    # draw existing groups
    def draw(self):
        self.screen.fill(BG)
        self.draw_grid()
        for sprite in self.entities:
            self.screen.blit(sprite.image, self.world.apply(sprite))
        pygame.display.flip()

    # set event loop for keyboard inputs
    def events(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()