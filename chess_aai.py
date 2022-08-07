import time
import pygame
import psettings

max_score = -0x7fffffff
min_score = -max_score
score_five = 10000

class chess_ai():
    def __init__(self, c_settings):
        self.len = c_settings.number
        self.record = [[[0, 0, 0, 0] for x in range(self.len)] for y in range(self.len)]
        self.count = [[0 for x in range(psettings.chess_type_number)] for i in range(2)]
        self.pop_score = [[(7 - max(abs(x - 7), abs(y - 7))) for x in range(c_settings.number)] for y in range(c_settings.number)]

    def is_win(self, board, player, psettings):
        return self.evaluate(board, player, psettings, True)

    def reset(self):
        for y in range(self.len):
            for x in range(self.len):
                for i in range(4):
                    self.record[y][x][i] = 0

        for i in range(len(self.count)):
            for j in range(len(self.count[0])):
                self.count[i][j] = 0

        self.save_count = 0

    def getmove(self, board, player):  # 获取所有空的位置
        move = []
        for y in range(self.len):
            for x in range(self.len):
                if board[y][x] == 0:
                    score = self.pop_score[y][x]
                    move.append((score, x, y))

        move.sort(reverse=True)
        return move

    def __search(self, board, player, depth, alpha=max_score, beta=min_score):
        score = self.evaluate(board, player, psettings)
        # print(score, player)
        if depth <= 0 or abs(score) > score_five:
            return score
        moves = self.getmove(board, player)
        bestmove = None
        self.alpha += len(moves)


        if len(moves) == 0:
            return score
        for _, x, y in moves:
            board[y][x] = player

            if player == psettings.chess_player.chess_player_one:
                opponent_play = psettings.chess_player.chess_player_two
            else:
                opponent_play = psettings.chess_player.chess_player_one
            score = -self.__search(board,opponent_play,depth-1,-beta,-alpha)
            # print(score)
            board[y][x] = 0
            self.belta += 1
            # print(self.belta)

            if score > alpha:
                alpha = score
                bestmove = (x, y)
                if alpha >= beta:
                    # return alpha
                    break
        if depth == self.maxdepth and bestmove:
            self.bestmove = bestmove
        return alpha

    def search(self, board, player,depth):
        self.bestmove = None
        self.maxdepth = depth
        score = self.__search(board, player, depth)
        x, y = self.bestmove
        # print(self.bestmove)
        return score, x, y

    def findbest(self, board, player, psettings, c_psettings):
        time1 = time.time()
        self.alpha = 0
        self.belta = 0
        score, x, y = self.search(board, player, c_psettings.depth)
        time2 = time.time()
        print('time[%.2f] (%d, %d), score[%d] ' % (
            (time2 - time1), x, y, score))
        return (x, y)


    def evaluate(self, board, player, psettings,check_win = False):
        self.reset()
        if player == psettings.chess_player.chess_player_one:
            mine = 1
            opponent = 2
        else:
            mine = 2
            opponent = 1

        for y in range(self.len):
            for x in range(self.len):
                if board[y][x] == mine:
                    self.evaluatepoint(board, x, y, mine, opponent, psettings)
                elif board[y][x] == opponent:
                    self.evaluatepoint(board, x, y, opponent, mine, psettings)

        mine_count = self.count[mine - 1]
        opponent_count = self.count[opponent - 1]
        if check_win:
            return mine_count[psettings.FIVE] > 0
        else:
            mscore, oscore = self.getscore(mine_count, opponent_count)
            # print(mine_count)
            # print(opponent_count)
            return (mscore - oscore)


    def evaluatepoint(self, board, x, y, mine, opponent, psettings):
        dir_reverse = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for i in range(4):
            if self.record[y][x][i] == 0:
                self.analysisline(board, x, y, i, dir_reverse[i], mine, opponent, self.count[mine - 1], psettings)
                # print(self.count)
            else:
                self.save_count += 1

    def getscore(self, mine_count, opponent_count):

        mscore, oscore = 0, 0
        if mine_count[psettings.FIVE] > 0:
            return (10000, 0)
        if opponent_count[psettings.FIVE] > 0:
            return (0, 10000)

        if mine_count[psettings.SFOUR] >= 2:
            mine_count[psettings.FOUR] += 1
        if opponent_count[psettings.SFOUR] >= 2:
            opponent_count[psettings.FOUR] += 1

        if mine_count[psettings.FOUR] > 0:
            return (9050,0)
        if mine_count[psettings.SFOUR] > 0:
            return (9040,0)

        if opponent_count[psettings.FOUR] > 0:
            return (0,9030)
        if opponent_count[psettings.SFOUR] > 0 and opponent_count[psettings.THREE] > 0:
            return (0, 9020)

        if mine_count[psettings.THREE] > 0 and opponent_count[psettings.SFOUR] == 0:
            return (9010,0)

        if (opponent_count[psettings.THREE] > 1 and mine_count[psettings.THREE] == 0 and mine_count[
            psettings.STHREE] == 0):
            return (0,9000)

        if opponent_count[psettings.SFOUR] > 0:
            oscore += 400

        if mine_count[psettings.THREE] > 1:
            mscore += 500

        if mine_count[psettings.THREE] > 0:
            mscore += 100

        if opponent_count[psettings.THREE] > 1:
            oscore += 2000

        if opponent_count[psettings.THREE] > 0:
            oscore += 400

        if mine_count[psettings.STHREE] > 0:
            mscore += mine_count[psettings.STHREE] * 10
        if opponent_count[psettings.STHREE] > 0:
            oscore += opponent_count[psettings.STHREE] * 10

        if mine_count[psettings.TWO] > 0:
            mscore += mine_count[psettings.TWO] * 6
        if opponent_count[psettings.TWO] > 0:
            oscore += opponent_count[psettings.TWO] * 6

        if mine_count[psettings.STWO] > 0:
            mscore += mine_count[psettings.STWO] * 2
        if opponent_count[psettings.STWO] > 0:
            oscore += opponent_count[psettings.STWO] * 2
        return (mscore, oscore)

    def getline(self, board, x, y, dir_reverse, mine, opponent):
        line = [0 for i in range(9)]
        tem_x = x + (-5*dir_reverse[0])
        tem_y = y + (-5*dir_reverse[1])
        for i in range(9):
            tem_x += dir_reverse[0]
            tem_y += dir_reverse[1]
            if (tem_x<0 or tem_x>=self.len or tem_y<0 or tem_y>=self.len):
                line[i] = opponent
            else:
                line[i] = board[tem_y][tem_x]
        return line

    def analysisline(self, board, x, y, dir_index, dir_reverse, mine, opponent, count, psettings):
        def setrecord(self, x, y, left, right, dir_index, dir_reverse):
            tem_x = x + (-5+left)*dir_reverse[0]
            tem_y = y + (-5+left)*dir_reverse[1]
            for i in range(left, right+1):
                tem_x += dir_reverse[0]
                tem_y += dir_reverse[1]
                self.record[tem_y][tem_x][dir_index] = 1

        empty = psettings.chess_player.chess_empty.value
        left_indx, right_indx = 4,4
        line = self.getline(board, x, y, dir_reverse, mine, opponent)

        while right_indx < 8:
            if line[right_indx+1] != mine:
                break
            right_indx += 1
        while left_indx > 0:
            if line[left_indx-1] != mine:
                break
            left_indx -= 1

        left_range, right_range = left_indx,right_indx
        while right_range < 8:
            if line[right_range+1] == opponent:
                break
            right_range += 1
        while left_range > 0:
            if line[left_range - 1] == opponent:
                break
            left_range -= 1
        chess_range = right_range - left_range+1  # 空格加自己格子
        if chess_range < 5:
            setrecord(self, x, y,left_range, right_range,dir_index,dir_reverse)
            return psettings.chess_type.NONE

        setrecord(self, x, y, left_indx, right_indx,dir_index,dir_reverse)
        m_range = right_indx - left_indx + 1  # 自己格连续数
        # p 代表敌人   m代表自己  x代表空
        # 活五
        if m_range == 5:   # mmmmm
            count[psettings.FIVE] += 1
        # 活四或者是冲四（2种）
        if m_range == 4:
            left_empty = right_empty = False
            if line[left_indx - 1] == empty:
                left_empty = True
            if line[right_indx+1] == empty:
                right_empty = True
            if left_empty and right_empty:
                count[psettings.FOUR] += 1  # xmmmx
            elif left_empty or right_empty:
                count[psettings.SFOUR] += 1 # xmmmp or pmmmx
            # 冲四或者活三（2种）或者冲三（2种）
        if m_range == 3:
            left_empty = right_empty = False
            left_four = right_four = False
            if line[left_indx - 1] == empty:
                if line[left_indx - 2] == mine:
                    setrecord(self, x, y, left_indx-2, left_indx - 1, dir_index,dir_reverse)
                    count[psettings.SFOUR] += 1  # mxmmm
                    left_four = True
                left_empty = True
            if line[right_indx+1] == empty:
                if line[right_indx + 2] == mine:  # mmmxm
                    setrecord(self, x, y, left_indx+1, left_indx+2,dir_index,dir_reverse)
                    count[psettings.SFOUR] += 1
                    right_four = True
                right_empty = True

            if left_four or right_four:
                pass
            elif left_empty and right_empty:
                if chess_range > 5:  # xmmmxx   xxmmmx
                    count[psettings.THREE] += 1
                else:
                    count[psettings.STHREE] += 1  # pxmmmxp
            elif left_empty or right_empty:
                count[psettings.STHREE] += 1  # pmmmx or xmmmp
        if m_range == 2:
            left_empty = right_empty = False
            left_three = right_three = False
            if line[left_indx - 1] == empty:
                if line[left_indx - 2] == mine:
                    setrecord(self, x, y, left_indx - 2, left_indx - 1, dir_index,dir_reverse)
                    if line[left_indx - 3] == empty:
                        if line[right_indx + 1] == empty:
                            count[psettings.THREE] += 1  # xmxmmx
                        else:
                            count[psettings.STHREE] += 1  # xmxmmp
                        left_three = True
                    elif line[left_indx - 3] == opponent:
                        if line[right_indx+1] == empty:
                            count[psettings.STHREE] += 1  # pmxmmx
                            left_three = True
                left_empty = True
            if line[right_indx+1] == empty:
                if line[right_indx + 2] == mine:
                    if line[right_indx+3] == mine:
                        setrecord(self,x, y, right_indx+1, right_indx+3, dir_index,dir_reverse)
                        count[psettings.SFOUR] += 1  # mmxmm
                        right_three = True
                    elif line[right_indx+3] == empty:
                        if left_empty:
                            count[psettings.THREE] += 1 # xmmxmx
                        else:
                            count[psettings.STHREE] += 1 # pmmxmx
                        right_three = True
                    elif left_empty:
                        count[psettings.STHREE] += 1 # xmmxmp
                        right_three = True
                right_empty = True
            if left_three or right_three:
                pass
            elif left_empty and right_empty:
                count[psettings.TWO] += 1  # xmmx
            elif left_empty or right_empty:
                count[psettings.STWO] +=1  # pmmx,xmmp

        if m_range == 1:
            left_empty = right_empty = False
            if line[left_indx - 1] == empty:
                if line[left_indx - 2] == mine:
                    if line[left_indx - 3] == empty:
                        if line[right_indx + 1] == opponent:
                            count[psettings.STWO] += 1 # xmxmp
                left_empty = True

            if line[right_indx + 1] == empty:
                if line[right_indx + 2] == mine:
                    if line[right_indx+3] == empty:
                        if left_empty:
                            count[psettings.TWO] += 1  # xmxmx
                        else:
                            count[psettings.STWO] += 1  # pmxmx
                elif line[right_indx+2] == empty:
                    if line[right_indx+3] == mine and line[right_indx+4] == empty:
                        count[psettings.TWO] += 1  # xmxxmx
        return psettings.chess_type.NONE

    """def search_best(self,board, player,psettings,c_psettings):
            moves = self.getmove(board,player)
            bestmove = None
            max_score = -0x7fffffff
            for score, x, y in moves:
                board[y][x] = player.value
                score = self.evaluate(board, player, psettings)
                board[y][x] = 0
                if score > max_score:
                    max_score = score
                    bestmove = (max_score,x,y)
            return bestmove


    def findbest(self, board, player, psettings,c_psettings):
            score, x, y = self.search_best(board,player,psettings,c_psettings)
            return (x, y)"""

"""    def getscore(self,mine_count, opponent_count):
        mscore, oscore = 0,0
        if mine_count[psettings.FIVE] > 0:
            return (10000,0)
        if opponent_count[psettings.FIVE] > 0:
            return (0,10000)

        if mine_count[psettings.SFOUR] >= 2:
            mine_count[psettings.FOUR] += 1
        if opponent_count[psettings.SFOUR] >= 2:
            opponent_count[psettings.FOUR] += 1

        if opponent_count[psettings.FOUR] >0:
            return (0,9050)
        if opponent_count[psettings.SFOUR]>0:
            return (0, 9040)

        if mine_count[psettings.FOUR]>0:
            return (9030,0)
        if mine_count[psettings.SFOUR]>0 and mine_count[psettings.THREE]>0:
            return (0,9020)

        if opponent_count[psettings.THREE]>0 and mine_count[psettings.SFOUR] == 0:
            return (0,9010)

        if (mine_count[psettings.THREE]>1 and opponent_count[psettings.THREE]==0 and opponent_count[psettings.STHREE] == 0):
            return(9000,0)

        if mine_count[psettings.SFOUR] >0:
            mscore+=2000

        if mine_count[psettings.THREE]>1:
            mscore+=500

        if mine_count[psettings.THREE]>0:
            mscore+=100

        if opponent_count[psettings.THREE]>1:
            oscore+=2000

        if opponent_count[psettings.THREE]>0:
            oscore+=400

        if mine_count[psettings.STHREE]>0:
            mscore+=mine_count[psettings.STHREE]*10
        if opponent_count[psettings.STHREE]>0:
            oscore+=opponent_count[psettings.STHREE]*10

        if mine_count[psettings.TWO]>0:
            mscore+=mine_count[psettings.TWO]*4
        if opponent_count[psettings.TWO]>0:
            oscore+=opponent_count[psettings.TWO]*4

        if mine_count[psettings.STWO]>0:
            mscore+=mine_count[psettings.STWO]*4
        if opponent_count[psettings.STWO]>0:
            oscore+=opponent_count[psettings.STWO]*4
        return (mscore, oscore)
"""
