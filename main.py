#code:utf-8
#author:zkl
import pygame
from pygame.locals import *
from enum import Enum
#颜色RGB
class Color(Enum):
    WHIHT = (255,255,255)
    BLACK = (0,0,0)
    RED = (255,0,0)
#棋子类
class chess():
    #初始化
    def __init__(self):
        pass
    #接受位置和颜色
    def set_pos(self,pos):
        self.pos = pos
    def get_pos(self,pos):
        return self.pos
    # 传出位置和颜色
    def set_color(self,color):
        self.color = color
    def get_color(self,color):
        return self.color
#棋盘类
class Chessboard():
    #行数和列数SIZE
    SIZE = 1
    #单元格大小UNIT
    UNIT = 1
    #初始化棋盘
    def __init__(self,size,unit):
        self.SIZE = size
        self.UNIT = unit

    # 绘制棋盘, 传入当前棋盘，窗口，边框宽度
    def drawmap(self, screen, width):
        # 行
        for row in range(self.SIZE):
            pygame.draw.line(screen, Color.RED.value,
                             (width, width + row * self.UNIT),
                             (width + self.UNIT * (self.SIZE - 1),
                              width + row * self.UNIT))
        # 列
        for column in range(self.SIZE):
            pygame.draw.line(screen, Color.RED.value,
                             (width + column * self.UNIT, width),
                             (width + column * self.UNIT,
                              width + self.UNIT * (self.SIZE - 1)))
#主程序
#初始化界面
from Chessboard.chessboard import Chessboard


def init_game():
    # 设置边框宽度
    BOARD_WIDTH = 50
    # 创建棋盘
    chessboard = Chessboard(10, 35)
    pygame.init()
    # 创建窗口
    screen = pygame.display.set_mode((2*BOARD_WIDTH+chessboard.UNIT*(chessboard.SIZE - 1),
                                      2*BOARD_WIDTH+chessboard.UNIT*(chessboard.SIZE - 1)))
    #设置窗口标题
    pygame.display.set_caption("我的五子棋AI果然有问题")
    #设置背景
    background = pygame.image.load('bg.jpg')
    screen.blit(background,(-100,-100))
    # #绘制棋盘
    Chessboard.drawmap(chessboard,screen,BOARD_WIDTH)
#控制游戏进程
if __name__ == '__main__':
    init_game()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        pygame.display.update()