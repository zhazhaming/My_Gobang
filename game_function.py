import pygame

import gamefunction as gf1

def get_one_dire_num(c_settings, last_x, last_y, dx, dy, m):
    tx = last_x
    ty = last_y
    count = 0
    while True:
        tx += dx
        ty += dy
        if tx < 0 or tx >= c_settings.number or ty < 0 or ty >= c_settings.number or m[ty][tx] == 0:
            return count
        count += 1

def check_win(chess_arr, c_settings):
    m = [[0] * c_settings.number for i in range(c_settings.number)]
    for x, y, c in chess_arr:
        if c == c_settings.chess_role:
            m[y][x] = 1  # 把（x， y， role）转换成一个矩阵
    last_x = chess_arr[-1][0]
    last_y = chess_arr[-1][1]
    dire_arr = [[(-1, 0), (1, 0)], [(0, -1), (0, 1)], [(-1, -1), (1, 1)], [(-1, 1), (1, -1)]]
    for dire1, dire2 in dire_arr:
        dx, dy = dire1
        num1 = get_one_dire_num(c_settings, last_x, last_y, dx, dy, m)
        dx, dy = dire2
        num2 = get_one_dire_num(c_settings, last_x, last_y, dx, dy, m)
        if num1+num2+1 >= 5:
            return True
    return False

def check_chess(c_settings, screen, chess_arr):
    x, y = pygame.mouse.get_pos()
    xi = int(round((x - c_settings.bg_left) * 1.0 / c_settings.bg_space))
    yi = int(round((y - c_settings.bg_top) * 1.0 / c_settings.bg_space))
    if xi >= 0 and xi < c_settings.number and yi >=0 and yi < c_settings.number and (xi, yi, 1) not in chess_arr and (xi, yi, 2)not in chess_arr:
        if c_settings.chess_role == 1:
            c_settings.chess_role = 2
        else:
            c_settings.chess_role = 1
        chess_arr.append((xi, yi, c_settings.chess_role))
        if check_win(chess_arr, c_settings):
            c_settings.game_start = 2 if c_settings.chess_role == 1 else 3 # start=1表示游戏进行 ，2表示白棋 3表示黑棋

def regret_game(c_settings, screen, c_button, c_blackboard,c_psettings, chess_arr, step):
    x_button, y_button = pygame.mouse.get_pos()
    button_click = c_button.play_button3_image_rect.collidepoint(x_button, y_button)
    if button_click == 1:
        if len(chess_arr) == 1:
            c_settings.chess_role = 1
        if len(chess_arr) > 0:
            chess_arr.pop()
            init_all(screen, c_blackboard, c_settings, c_button)
            draw_chess(c_settings, screen, chess_arr)
        if len(step) > 0:
            gf1.reset_player_mark(c_psettings, c_settings, step)
            if len(step) >= 2:
                del step[-2:]
            gf1.draw_chess(screen, c_psettings, c_settings, step)
            init_all(screen, c_blackboard, c_settings, c_button)

def replay_game(c_settings, screen, c_button, c_blackboard,c_psettings, chess_arr, step):
    x_button, y_button = pygame.mouse.get_pos()
    button_click = c_button.play_button_image_rect.collidepoint(x_button, y_button)
    if button_click == 1:
        c_settings.have_win = False
        c_settings.chess_role = 1  # 重新回到黑子落子
        chess_arr.clear()
        step.clear()
        c_psettings.depth = 0
        gf1.reset_map(c_settings, c_psettings)
        init_all_change(screen, c_blackboard, c_settings, c_button)
        c_settings.can_chose = True
        c_settings.who_first = False
        c_psettings.player = 0
        x_button, y_button = pygame.mouse.get_pos()
        button_click_play = c_button.play_button1_image_rect.collidepoint(x_button, y_button)
        button_click_cvp = c_button.play_button1_image_rect.collidepoint(x_button, y_button)
        if button_click_play == 1:
            c_settings.game_active = 1
            c_settings.game_start = 1
            c_settings.chess_role = 1 # 重新回到黑子落子

        if button_click_cvp == 1:
            c_settings.game_active = 2
            c_psettings.winner = None
            # init_all(screen,c_blackboard,c_settings,c_button)



def is_game(screen, c_settings,chess_arr):
    if c_settings.game_start != 1:
        my_font = pygame.font.Font(None, 60)
        color_text = (210, 210, 0)
        win_text = "%s win" % ('white' if c_settings.game_start == 2 else 'black')
        text_image = my_font.render(win_text, True, color_text)

        screen.blit(text_image, (260, 320))
        c_settings.game_active = 0
        c_settings.have_win = True

def draw_chess(c_setting, screen, chess_arr):
    for x, y, c_setting.chess_role in chess_arr:
        chess_color = (0, 0, 0) if c_setting.chess_role == 2 else (200, 200, 200)
        pygame.draw.circle(screen, chess_color, [x*c_setting.bg_space+c_setting.bg_left,
                                                    y*c_setting.bg_space+c_setting.bg_top], 20, 20)

def draw_small_circle_1(screen):
    small_circle_color = (0, 0, 0)
    pygame.draw.circle(screen, small_circle_color, (810, 310), 7)

def draw_small_circle_2(screen):
    small_circle_color = (0, 0, 0)
    pygame.draw.circle(screen, small_circle_color, (810, 360), 7)

def click_play_button(screen, c_button, c_settings, c_psettings,c_blackboard, chess_arr,step):
    x_button, y_button = pygame.mouse.get_pos()
    button_click = c_button.play_button1_image_rect.collidepoint(x_button, y_button)
    if button_click == 1:
        c_settings.game_active = 1
        c_settings.game_start = 1
        if len(step) != 0:
            step.clear()
            gf1.reset_map(c_settings, c_psettings)
            init_all(screen, c_blackboard, c_settings, c_button)

def click_cvp_button(screen, c_button, c_settings,c_blackboard, chess_arr, c_psettings):
    x_button, y_button = pygame.mouse.get_pos()
    button_click = c_button.play_button2_image_rect.collidepoint(x_button, y_button)
    if button_click == 1:
        c_psettings.winner = None
        c_settings.game_active = 2
        c_psettings.is_play = True
        c_button.draw_small_circle()
        if len(chess_arr) != 0:
            chess_arr.clear()
            c_settings.chess_role = 1
            init_all(screen, c_blackboard, c_settings, c_button)

def click_m_button(screen, c_button, c_psettings,c_settings):
    x_button, y_button = pygame.mouse.get_pos()
    button_click = c_button.play_button4_image_rect.collidepoint(x_button, y_button)
    if button_click == 1:
        c_psettings.depth = 2
        c_settings.can_chose = False

def click_h_button(screen, c_button, c_psettings,c_settings):
    x_button, y_button = pygame.mouse.get_pos()
    button_click = c_button.play_button5_image_rect.collidepoint(x_button, y_button)
    if button_click == 1:
        c_psettings.depth = 3
        c_settings.can_chose = False

def click_small_circle_1(screen, c_button,c_psettings,c_settings):
    x_button, y_button = pygame.mouse.get_pos()
    button_click = c_button.choose_small_circle_rect_1.collidepoint(x_button, y_button)
    if button_click == 1:
        draw_small_circle_1(screen)
        c_psettings.player = 1
        c_settings.who_first = True
        c_settings.first_choose = 'white'

def click_small_circle_2(screen,c_button,c_psettings,c_settings):
    x_button, y_button = pygame.mouse.get_pos()
    button_click = c_button.choose_small_circle_rect_2.collidepoint(x_button, y_button)
    if button_click == 1:
        draw_small_circle_2(screen)
        c_psettings.player = 2
        c_settings.who_first = True
        c_settings.first_choose = 'black'




def init_all(screen, c_blackboard,c_settings, c_button):
    c_blackboard.dawmap(c_settings, screen)
    c_button.draw_button1()
    c_button.draw_button2()
    c_button.draw_play_button()
    c_button.draw_button3()
    c_button.draw_button4()
    c_button.draw_button5()
    c_button.draw_small_circle()

def init_all_change(screen, c_blackboard,c_settings, c_button):  #用于replay处
    c_blackboard.dawmap(c_settings, screen)
    c_button.draw_button1()
    c_button.draw_button2()
    c_button.draw_play_button()
    c_button.draw_button3()
    c_button.draw_button4()
    c_button.draw_button5()


"""x, y = pygame.mouse.get_pos()
    x1 = int(round((x - c_settings.bg_left) * 1.0 / c_settings.bg_space))
    y1 = int(round((y - c_settings.bg_top) * 1.0 / c_settings.bg_space))
    x1 = chess_arr[-1][0]
    y1 = chess_arr[-1][1]

    # 横向
    for x in range(x1 - 4):
        for y in range(y1):
            if c_settings.count > 8 and m[y][x] == m[y][x+1] == m[y][x+2] == m[y][x+3] == m[y][x+4] == 2:
                return 'black_win'
            if c_settings.count > 8 and m[y][x] == m[y][x+1] == m[y][x+2] == m[y][x+3] == m[y][x+4] == 1:
                return 'white_win'
    # 竖向
    for x in range(x1):
        for y in range(y1 - 4):
            if c_settings.count > 8 and m[y][x] == m[y+1][x] == m[y+2][x] == m[y+3][x] == m[y+4][x] == 2:
                return 'black_win'
            if c_settings.count > 8 and m[y][x] == m[y+1][x] == m[y+2][x] == m[y+3][x] == m[y+4][x] == 1:
                return 'white_win'
    # 右上到左下
    for x in range(x1 - 4):
        for y in range(y1 - 4):
            if c_settings.count > 8 and m[y][x+4] == m[y+1][x+3] == m[y+2][x+2] == m[y+3][x+1] == m[y+4][x] == 2:
                return 'black_win'
            if c_settings.count > 8 and m[y][x] == m[y+1][x] == m[y+2][x] == m[y+3][x] == m[y+4][x] == 1:
                return 'white_win'
   # 左上到右下
    for x in range(x1 - 4):
        for y in range(y1 - 4):
            if c_settings.count > 8 and m[y][x] == m[y+1][x+1] == m[y+2][x+2] == m[y+3][x+3] == m[y+4][x+4] == 2:
                return 'black_win'
            if c_settings.count > 8 and m[y][x] == m[y+1][x+1] == m[y+2][x+2] == m[y+3][x+3] == m[y+4][x+4] == 1:
                return 'white_win'"""