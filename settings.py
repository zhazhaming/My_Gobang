from enum import IntEnum
# from chess_ai import *

class Settings():
    def __init__(self):
        # 屏幕的长宽和背景颜色
        self.screen_width = 1100
        self.screen_heigh = 800
        self.bg_color = (204,232,207)
        # 文字大小
        self.fontsize = 14
        self.fonttype = 'simsunnsimsun'
        # 棋盘格数
        self.number = 15
        # 棋盘的左、顶边距和间距
        self.bg_left = 50
        self.bg_top = 50
        self.bg_space = 50
        self.map_width = self.number * self.bg_space
        self.map_height = self.number * self.bg_space
        # 棋子
        self.chess_role = 1  # 1为白，2为黑
        # 棋子步数
        self.count = 0
        # 如果任意一种模式赢就变成假
        self.have_win = False
        # 判断游戏是否结束
        self.game_start = 1 # 1代表游戏进行，2代表白棋，3代表黑棋
        # 开始时为0，不可下子
        self.game_active = 0  # 0表示全部游戏结束，1表示人人游戏进行，2表示人机游戏进行
        # 是否能选择模式
        self.can_chose = True
        # 按钮按下颜色
        self.button_color = (204, 232, 207)
        # 电脑执黑还是执白
        self.who_first = False
        # 记录落子第一个是什么颜色的棋子
        self.first_choose = None




"""class map():
    def __init__(self):
        self.map = [[0 for x in range(15)] for y in range(15)]
        self.steps = []
        self.isplay = False
        self.AI = ChessAI(15)
        self.useAI = False
        self.winner = None

        self.play_empty = 0
        self.player_one = 1
        self.player_two = 2
        self.player_none = 3

    def reset(self):
        for y in range(15):
            for x in range(15):
                self.map[y][x] = 0
        self.steps = []

    def reverseTurn(self, turn):
        if turn == self.player_one:
            return self.player_two
        else:
            return self.player_two

    def click(self, x, y, type):
        self.map[y][x] = type.value
        self.steps.append((x, y))
"""
