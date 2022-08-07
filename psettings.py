import pygame
from enum import IntEnum

class chess_player(IntEnum):
    chess_empty = 0
    chess_player_one = 1 # 黑棋
    chess_player_two = 2  # 白棋
    chess_player_NONE = 3

class chess_type(IntEnum):
    NONE = 0
    sleep_two = 1
    live_two = 2
    sleep_three = 3
    live_three = 4
    chong_four = 5
    live_four = 6
    live_five = 7

chess_type_number = 8
FIVE = chess_type.live_five.value
FOUR, THREE, TWO = chess_type.live_four.value, chess_type.live_three.value, chess_type.live_two.value
SFOUR, STHREE, STWO = chess_type.chong_four.value, chess_type.sleep_three.value, chess_type.sleep_two.value

class psettings():
    def __init__(self):
        self.is_play = False
        self.player = 0  # 1表示人，2表示电脑,0表示待定
        self.map = [[0 for x in range(15)] for y in range(15)]
        self.winner = None
        self.max_score = -0x7fffffff
        self.min_score = -self.max_score
        self.depth = 0
        self.bestmove = None
        """self.alpha = 0
        self.beta = 0"""