import time
import pygame
import psettings
from button import Button

# 用于保存棋谱

def reset_map(c_settings,c_psettings):
    for y in range(c_settings.number):
        for x in range(c_settings.number):
            c_psettings.map[y][x] = 0

def reset_player_mark(c_psettings,c_settings,step):
    if len(step) >= 2:
        for x, y, player in step:
            x = step[-1][0]
            y = step[-1][1]
            xi = step[-2][0]
            yi = step[-2][1]
            c_psettings.map[y][x] = 0
            c_psettings.map[yi][xi] = 0

def change_chess(c_psettings):
    if c_psettings.player == 1:
        return c_psettings.player == 2
    else:
        return c_psettings.player == 1

def draw_chess(screen, c_psettings, c_settings, step):
    for x, y, player in step:
        if step[0][2] == 1:
            color = (0, 0, 0) if player == 1 else (200, 200, 200)
        if step[0][2] == 2:
            color = (0, 0, 0) if player == 2 else (200, 200, 200)
        pygame.draw.circle(screen, color, [x * c_settings.bg_space + c_settings.bg_left,
                                                 y * c_settings.bg_space + c_settings.bg_top], 20, 20)

def draw_small_line(screen, c_settings, step):
    if len(step) == 0:
        pass
    if len(step) > 0:
        x = step[-1][0]
        y = step[-1][1]
        x_chess = x*c_settings.bg_space+c_settings.bg_left
        y_chess = y*c_settings.bg_space+c_settings.bg_top
        line_color = (255, 0, 0)
        begin_1 = (x_chess-22, y_chess-22)
        end_1 = (x_chess+22, y_chess-22)
        begin_2 = (x_chess+22, y_chess-22)
        end_2 = (x_chess+22, y_chess+22)
        begin_3 = (x_chess+22, y_chess+22)
        end_3 = (x_chess-22, y_chess+22)
        begin_4 = (x_chess-22, y_chess+22)
        end_4 = (x_chess-22, y_chess-22)
        pygame.draw.line(screen, line_color, begin_1, end_1, 1)
        pygame.draw.line(screen, line_color, begin_2, end_2, 1)
        pygame.draw.line(screen, line_color, begin_3, end_3, 1)
        pygame.draw.line(screen, line_color, begin_4, end_4, 1)

def init(screen,c_settings,c_psettings,c_button,c_blackboard,step):

    if len(step) > 0:
        c_blackboard.dawmap(c_settings, screen)
        c_button.draw_button1()
        c_button.draw_button2()
        c_button.draw_play_button()
        c_button.draw_button3()
        c_button.draw_button4()
        c_button.draw_button5()
        c_button.draw_small_circle()
        draw_small_line(screen, c_settings, step)


def check_win(c_ai, board, player, psettings,c_psettings,step):
    if c_ai.is_win(board, player, psettings) and c_psettings.winner == None:
        c_psettings.winner = player

    if c_psettings.winner == None and len(step) >= 225:
        c_psettings.winner = 3

def show_win(screen, c_psettings,c_settings,psettings,step):
    if c_settings.first_choose == 'white':
        if c_psettings.winner == psettings.chess_player.chess_player_one.value:
            my_font = pygame.font.Font(None, 60)
            color_text = (210, 210, 0)
            win_text = "black win_p"
            text_image = my_font.render(win_text, True, color_text)
            screen.blit(text_image, (260, 320))
            c_settings.game_active = 0
            c_settings.have_win = True
        if c_psettings.winner == psettings.chess_player.chess_player_two.value:
            my_font = pygame.font.Font(None, 60)
            color_text = (210, 210, 0)
            win_text = "white win_p"
            winner = "white"
            text_image = my_font.render(win_text, True, color_text)
            screen.blit(text_image, (260, 320))
            c_settings.game_active = 0
            c_settings.have_win = True
        if c_psettings.winner == 3:
            my_font = pygame.font.Font(None, 60)
            color_text = (210, 210, 0)
            win_text = "he qi"
            winner = "heqi"
            text_image = my_font.render(win_text, True, color_text)
            screen.blit(text_image, (260, 320))
            c_settings.game_active = 0
            c_settings.have_win = True
    if c_settings.first_choose == 'black':
        if c_psettings.winner == psettings.chess_player.chess_player_one.value:
            my_font = pygame.font.Font(None, 60)
            color_text = (210, 210, 0)
            win_text = "white win_p"
            winner = "white"
            text_image = my_font.render(win_text, True, color_text)
            screen.blit(text_image, (260, 320))
            c_settings.game_active = 0
            c_settings.have_win = True
        if c_psettings.winner == psettings.chess_player.chess_player_two.value:
            my_font = pygame.font.Font(None, 60)
            color_text = (210, 210, 0)
            win_text = "black win_p"
            winner = "black"
            text_image = my_font.render(win_text, True, color_text)
            screen.blit(text_image, (260, 320))
            c_settings.game_active = 0
            c_settings.have_win = True
        if c_psettings.winner == 3:
            my_font = pygame.font.Font(None, 60)
            color_text = (210, 210, 0)
            win_text = "he qi"
            winner = "heqi"
            text_image = my_font.render(win_text, True, color_text)
            screen.blit(text_image, (260, 320))
            c_settings.game_active = 0
            c_settings.have_win = True

def play( c_psettings, c_settings,  c_ai, step):
    if c_psettings.is_play == True:
        if c_psettings.player == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            xi = int(round((mouse_x - c_settings.bg_left) * 1.0 / c_settings.bg_space))
            yi = int(round((mouse_y - c_settings.bg_top) * 1.0 / c_settings.bg_space))
            if xi >= 0 and xi < c_settings.number and yi >= 0 and yi < c_settings.number and (xi, yi, 1) not in step and (xi, yi, 2)not in step:
                c_psettings.map[yi][xi] = psettings.chess_player.chess_player_one.value
                check_win(c_ai, c_psettings.map, psettings.chess_player.chess_player_one, psettings, c_psettings, step)
                step.append((xi, yi, psettings.chess_player.chess_player_one.value))
                c_psettings.player = 2
        if c_psettings.player == 2:
            x, y = c_ai.findbest(c_psettings.map, psettings.chess_player.chess_player_two, psettings,c_psettings)
            if x >= 0 and x < c_settings.number and y >=0 and y < c_settings.number and (x, y, 2)not in step and (x, y, 1)not in step:
                c_psettings.map[y][x] = psettings.chess_player.chess_player_two.value
                check_win(c_ai, c_psettings.map, psettings.chess_player.chess_player_two, psettings, c_psettings, step)
                step.append((x, y, psettings.chess_player.chess_player_two.value))
                c_psettings.player = 1
        print(step)

def game_save(c_settings,c_psettings,step):
    if(c_psettings.winner != None):
        result = []
        xi = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]
        yi = ["15", "14", "13", "12", "11", "10", "9", "8", "7", "6", "5", "4", "3", "2", "1"]
        for i in range(len(step)):
            playerr = None
            x_1, y_1, player = step[i]
            if c_settings.first_choose == 'black':
                if player == 2:
                    playerr = "B"
                if player == 1:
                    playerr = "W"
            if c_settings.first_choose == "white":
                if player == 1:
                    playerr = "B"
                if player == 2:
                    playerr = "W"
            x = xi[x_1]
            y = yi[y_1]
            r = playerr + "({},{})".format(x, y)
            result.append(r)
        if c_settings.first_choose == 'white'and c_psettings.winner == psettings.chess_player.chess_player_two.value:
            title = "C5-先手队B vs 保卫吾环变成王W-先手胜-"+time.strftime('%Y-%m-%d %H_%M_%S', time.localtime())+"五子棋.txt"
            with open("result/"+title,"w")as f:
                f.write("[C5][先手队 B][保卫吾环变成王W][先手胜][{}][2022 CCGC];".format(
                    time.strftime('%Y-%m-%d %H_%M_%S', time.localtime()))+ str(result))
        if c_settings.first_choose == 'black' and c_psettings.winner == psettings.chess_player.chess_player_one.value:
            title = "C5-先手队B vs 保卫吾环变成王W-后手胜-" + time.strftime('%Y-%m-%d %H_%M_%S', time.localtime()) + "五子棋.txt"
            with open("result/"+title,"w")as f:
                f.write("[C5][先手队 B][保卫吾环变成王W][后手胜][{}][2022 CCGC];".format(
                    time.strftime('%Y-%m-%d %H_%M_%S', time.localtime())) + str(result))

        if c_settings.first_choose == 'black' and c_psettings.winner == psettings.chess_player.chess_player_two.value:
            title = "C5-保卫吾环变成王B vs 先手队W-先手胜-" + time.strftime('%Y-%m-%d %H_%M_%S', time.localtime()) + "-五子棋.txt"
            with open("result/"+title, "w")as f:
                f.write("[C5][保卫吾环变成王 B][后手队 W][先手胜][{}][2022 CCGC];".format(
                    time.strftime('%Y-%m-%d %H_%M_%S', time.localtime())) + str(result))

        if c_settings.first_choose == 'black' and c_psettings.winner == psettings.chess_player.chess_player_one.value:
            title = "C5-保卫吾环变成王B vs 先手队W-后手胜-" + time.strftime('%Y-%m-%d %H_%M_%S', time.localtime()) + "五子棋.txt"
            with open("result/"+title, "w")as f:
                f.write("[C5][保卫吾环变成王 B][后手队 W][后手胜][{}][2022 CCGC];".format(
                    time.strftime('%Y-%m-%d %H_%M_%S', time.localtime())) + str(result))

