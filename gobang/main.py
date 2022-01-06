# -*- coding: utf-8 -*-
# @Time     :2022/1/6 22:24
# @Author   :Z
# @File     :main.py
import pygame

# 棋子
_BLACK = 1
_BLANK = 0
_WHITE = -1

# 颜色


class gobang():
    def __init__(self):
        # 棋盘与棋子的大小
        self.cell_size = 60
        self.cell_num = 15
        self.space_size = 80
        self.grid_length = self.cell_size * (self.cell_num - 1) + self.space_size * 2

        # 设置棋子在后台的位置，初始全部为空
        self.chess_pos = []
        self.initChessBoard()
        # 设置AI
        self.use_AI = False
        self.AI_turn = _WHITE

    def initChessBoard(self):
        for i in range(self.cell_num):
            self.chess_pos.append([_BLANK] * self.cell_num)

    def warning(self, chess):
        # print("这个位置已经有{}棋了".format("黑" if chess == _BLACK else "白"))
        pass

    def judgeWin(self, x_i, y_i):
        dir = [
            [[-1, 0], [1, 0]],
            [[0, -1], [0, 1]],
            [[-1, -1], [1, 1]],
            [[1, -1], [-1, 1]]
        ]
        cur_x_i = x_i
        cur_y_i = y_i

        for i in range(4):
            count = 1
            for j in range(2):
                # 某一个方向查找
                while True:
                    cur_x_i += dir[i][j][0]
                    cur_y_i += dir[i][j][1]
                    # 处于界内
                    if 0 <= cur_x_i < self.cell_num and 0 <= cur_y_i < self.cell_num:
                        # 颜色相同,则继续
                        if self.chess_pos[cur_x_i][cur_y_i] == self.turn:
                            count += 1
                            continue
                        else:
                            # 停止此次循环，相对应的下一个方向
                            break
                    else:
                        break

                # 将当前游标复位
                cur_x_i = x_i
                cur_y_i = y_i

            if count >= 5:
                return True

        return False



    def run(self):
        self.screen = pygame.display.set_mode((self.grid_length, self.grid_length))
        self.turn = _BLACK
        while True:

            if self.use_AI == True and self.turn == self.AI_turn:
                # AI落子
                pass
            else:
                # 人类落子
                for event in pygame.event.get():
                    # 如果是退出事件
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    # 如果是鼠标单击事件
                    if event.type == pygame.MOUSEBUTTONUP:
                        x_pos, y_pos = pygame.mouse.get_pos()
                        print(x_pos, y_pos)
                        x_i = int(round((x_pos - self.space_size) / self.cell_size))
                        y_i = int(round((y_pos - self.space_size) / self.cell_size))
                        print(x_i, y_i)
                        if 0 <= x_i < self.cell_num and 0 <= y_i < self.cell_num:
                            # 如果是个空位置
                            if self.chess_pos[x_i][y_i] == _BLANK:
                                self.chess_pos[x_i][y_i] = self.turn
                                # 落子完成后，要判断是否已经胜了
                                if self.judgeWin(x_i, y_i):
                                    print("win")

                                # 换边
                                self.turn = -self.turn

                            else:
                                self.warning(self.chess_pos[x_i][y_i])

            # 显示界面为淡蓝色，棋盘线为白色
            self.screen.fill((0, 121, 121))
            for x in range(0, self.cell_num * self.cell_size, self.cell_size):
                pygame.draw.line(
                    self.screen,
                    (200, 200, 200),
                    (x + self.space_size, 0 + self.space_size),
                    (x + self.space_size, self.cell_size * (self.cell_num - 1) + self.space_size),
                    1
                )

            for y in range(0, self.cell_num * self.cell_size, self.cell_size):
                pygame.draw.line(
                    self.screen,
                    (200, 200, 200),
                    (0 + self.space_size, y + self.space_size),
                    (self.cell_size * (self.cell_num - 1) + self.space_size, y + self.space_size),
                    1
                )

            # 画棋子的位置
            for x in range(self.cell_num):
                for y in range(self.cell_num):
                    color = None
                    if(self.chess_pos[x][y] == _BLANK):
                        continue
                    elif self.chess_pos[x][y] == _WHITE:
                        color = (205, 205, 205)
                    else:
                        color = (30, 30, 30)

                    x_pos = self.space_size + x * self.cell_size
                    y_pos = self.space_size + y * self.cell_size
                    pygame.draw.circle(self.screen, color, (x_pos, y_pos), 24, 24)

            pygame.display.update()

if __name__ == "__main__":
    game = gobang()
    game.run()