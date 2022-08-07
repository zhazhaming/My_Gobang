import pygame
from settings import Settings


class blackboard():
    def __init__(self, screen, c_settings):
        self.screen = screen
        self.c_settings = c_settings
        self.bg_image = pygame.image.load('image/blackboard.png').convert_alpha()
        # self.map = [[0 for x in range(self.c_settings.number)] for y in range(self.c_settings.number)]

    def dawmap(self, c_settings, screen):
        screen.fill(c_settings.bg_color)
        self.bg_image = pygame.transform.scale(self.bg_image, (800, 800))
        self.screen.blit(self.bg_image, (0, 0))
        color = (0, 0, 0)
        width = 2
        for i in range(c_settings.number):
           begin = (c_settings.bg_left+i*c_settings.bg_space, c_settings.bg_top)
           end = (c_settings.bg_left+i*c_settings.bg_space, c_settings.bg_space*c_settings.number)
           pygame.draw.line(screen, color, begin, end, width)

        for j in range(c_settings.number):
            begin = (c_settings.bg_left, c_settings.bg_top+j * c_settings.bg_space)
            end = (c_settings.bg_space*c_settings.number, c_settings.bg_space*j+c_settings.bg_top)
            pygame.draw.line(screen, color, begin, end, width)




"""class Map():
    def __init__(self, c_settings):
        self.c_settings = c_settings
        self.map = [[0 for x in range(c_settings.number)] for y in range(c_settings.number)]
        self.steps = []

    def reset(self, c_settings):
        for y in range(c_settings.number):
            for x in range(c_settings.number):
                self.map[y][x] = 0
        self.steps = []

    def click(self, x, y, type):
        self.map[y][x] = type.value
        self.steps.append((x, y))"""














