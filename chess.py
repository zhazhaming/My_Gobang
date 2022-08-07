import pygame
import sys
import settings
import psettings
import chess_aai
from blackboard import blackboard
from button import Button
import game_function as gf
import gamefunction as gf1


def run_game():
    pygame.init()
    c_settings = settings.Settings()
    screen = pygame.display.set_mode((c_settings.screen_width, c_settings.screen_heigh))
    c_blackboard = blackboard(screen, c_settings)
    c_button = Button(screen, c_settings)
    c_psettings = psettings.psettings()
    c_ai = chess_aai.chess_ai(c_settings)
    chess_arr = []
    step = []
    pygame.display.set_caption("五子棋")
# 绘图
    c_blackboard.dawmap(c_settings, screen)
    c_button.draw_button1()
    c_button.draw_button2()
    c_button.draw_play_button()
    c_button.draw_button3()
    c_button.draw_button4()
    c_button.draw_button5()
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                gf.replay_game(c_settings, screen, c_button, c_blackboard, c_psettings, chess_arr, step)

                if c_settings.have_win == False:
                    gf.click_play_button(screen, c_button, c_settings, c_psettings, c_blackboard, chess_arr,step)
                    gf.click_cvp_button(screen, c_button, c_settings, c_blackboard, chess_arr, c_psettings)
                    gf.regret_game(c_settings, screen, c_button, c_blackboard, c_psettings, chess_arr, step)
                    if c_settings.who_first == False:
                        gf.click_small_circle_1(screen, c_button, c_psettings, c_settings)
                        gf.click_small_circle_2(screen, c_button, c_psettings, c_settings)
                    if c_settings.can_chose == True:
                        gf.click_m_button(screen, c_button, c_psettings, c_settings)
                        gf.click_h_button(screen, c_button, c_psettings, c_settings)

                if c_settings.game_active == 1:
                    gf.check_chess(c_settings, screen, chess_arr)
                if c_settings.game_active == 2 and c_psettings.depth != 0:
                    gf1.play( c_psettings, c_settings, c_ai, step)
            if c_settings.game_active == 1:
                gf.draw_chess(c_settings, screen, chess_arr)
                gf.is_game(screen, c_settings, chess_arr)
            if c_settings.game_active == 2:
                gf1.init(screen, c_settings, c_psettings, c_button, c_blackboard, step)
                gf1.draw_chess(screen, c_psettings, c_settings, step)
                gf1.draw_small_line(screen, c_settings, step)
                gf1.show_win(screen, c_psettings, c_settings, psettings, step)
            if(c_psettings.winner!= None):
                gf1.game_save(c_settings, c_psettings, step)

        pygame.display.update()
        # pygame.display.flip()


run_game()
