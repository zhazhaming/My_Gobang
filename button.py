import pygame
from settings import Settings

class Button():
    def __init__(self, screen, c_settings):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.font = pygame.font.SysFont(None, 30)
        self.font1 = pygame.font.Font(None, 30)
        self.play_button_image = pygame.image.load("image/replay.png").convert_alpha()
        self.play_button1_image = pygame.image.load("image/p.png").convert_alpha()
        self.play_button2_image = pygame.image.load("image/c.png").convert_alpha()
        self.play_button3_image = pygame.image.load("image/r.png").convert_alpha()
        self.play_button4_image = pygame.image.load("image/medium.png").convert_alpha()
        self.play_button5_image = pygame.image.load("image/hard.png").convert_alpha()
        self.text_1 = self.font.render("white", True, (0, 0, 0))
        self.text_2 = self.font.render("black", True, (0, 0, 0))
        self.play_button_image_rect = pygame.Rect(900, 550, 155, 50)
        self.play_button1_image_rect = pygame.Rect(900, 200, 100, 60)
        self.play_button2_image_rect = pygame.Rect(900, 300, 100, 60)
        self.play_button3_image_rect = pygame.Rect(900, 450, 100, 60)
        self.play_button4_image_rect = pygame.Rect(900, 350, 100, 60)
        self.play_button5_image_rect = pygame.Rect(900, 400, 100, 60)
        self.choose_small_circle_rect_1 = pygame.Rect(800, 300, 15, 15)
        self.choose_small_circle_rect_2 = pygame.Rect(800, 350, 15, 15)
        self.play_button_share_bg_color = (0, 255, 0)
        self.play_button_share_color = (50, 150, 200)


    def draw_play_button(self):
        # self.play_button_image = self.font1.render("Start", True, self.play_button_share_color,self.play_button_share_bg_color)
        self.play_button_image = pygame.transform.scale(self.play_button_image, (155, 50))
        self.screen.blit(self.play_button_image, self.play_button_image_rect)

    def draw_button1(self):
        # self.play_button1_image = self.font1.render("People", True, self.play_button_share_color, self.play_button_share_bg_color)
        self.screen.blit(self.play_button1_image, self.play_button1_image_rect)

    def draw_button2(self):
        # self.play_button2_image = self.font1.render('Computer', True, self.play_button_share_color, self.play_button_share_bg_color)
        self.screen.blit(self.play_button2_image, self.play_button2_image_rect)

    def draw_button3(self):
        # self.play_button3_image = self.font1.render('Regret', True, self.play_button_share_color, self.play_button_share_bg_color)
        self.screen.blit(self.play_button3_image, self.play_button3_image_rect)

    def draw_button5(self):
        self.screen.blit(self.play_button5_image, self.play_button5_image_rect)

    def draw_button4(self):
        self.screen.blit(self.play_button4_image, self.play_button4_image_rect)

    def draw_small_circle(self):
        pygame.draw.circle(self.screen, (0, 0, 0), (810, 310), 10, 1)
        pygame.draw.circle(self.screen, (0, 0, 0), (810, 360), 10, 1)
        self.screen.blit(self.text_1, (830, 300))
        self.screen.blit(self.text_2, (830, 350))







