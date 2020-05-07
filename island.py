# _*_ coding: utf-8 _*_
import pygame
import numpy as np
from pygame.locals import *

class Array2D:
    """
        说明：
            1.构造方法需要两个参数，即二维数组的宽和高
            2.成员变量w和h是二维数组的宽和高
            3.使用：‘对象[x][y]’可以直接取到相应的值
            4.数组的默认值都是0
    """

    def __init__(self, w, h, default=0):
        self.w = w
        self.h = h
        self.data = []
        self.data = [[default for y in range(h)] for x in range(w)]

    def show_array2d(self):
        for y in range(self.h):
            for x in range(self.w):
                print(self.data[x][y], end=' ')
            print("")

    def __getitem__(self, item):
        return self.data[item]


class GameMap(Array2D):
    """
    游戏地图类
    """

    def __init__(self, bottom, top, x, y):
        # 将地图划分成w*h个小格子，每个格子32*32像素
        w = int(bottom.get_width() / 4) + 1
        h = int(top.get_height() / 4) + 1
        super().__init__(w, h)
        self.bottom = bottom
        self.top = top
        self.x = x
        self.y = y

    def draw_bottom(self, screen_surf):
        screen_surf.blit(self.bottom, (self.x, self.y))

    def draw_top(self, screen_surf):
        screen_surf.blit(self.top, (self.x, self.y))

    def draw_grid(self, screen_surf):
        """
        画网格
        """
        for x in range(self.w):
            for y in range(self.h):
                if self[x][y] == 0:
                    pygame.draw.rect(screen_surf, (255, 255, 255), (self.x + x * 32, self.y + y * 32, 32, 32), 1)
                else:
                    pygame.draw.rect(screen_surf, (0, 0, 0, 100), (self.x + x * 32 + 1, self.y + y * 32 + 1, 30, 30), 0)

    def load_walk_file(self, path):
        """
        读取可行走区域文件
        """
        # with open(path, 'r') as file:
            # for x in range(self.w):
                # for y in range(self.h):
                    # v = int(file.readline())
        matrix = np.zeros([313,169]).astype(int)
        for i in range(self.w):
        	for j in range(self.h):
        		self[i][j] = matrix[i][j]
        # self.show_array2d()

    def move(self, pressed_keys, player, WIN_WIDTH=640, WIN_HEIGHT=480):
        if (pressed_keys[K_UP] or pressed_keys[K_w]):
            if self.y + 4 < 0:
                self.y += 4
                print(self.x, self.y)
            else:
                self.y = 0
                player.move(pressed_keys)
                print(self.x, self.y)
        if (pressed_keys[K_DOWN] or pressed_keys[K_s]):
            if self.y - 4 > -188:
                self.y -= 4
                print(self.x, self.y)
            else:
                self.y = -(self.bottom.get_height() - WIN_HEIGHT)
                player.move(pressed_keys)
                print(self.x, self.y)
        if (pressed_keys[K_LEFT] or pressed_keys[K_a]):
            if self.x + 4 < 0:
                self.x += 4
                print(self.x, self.y)
            else:
                self.x = 0
                player.move(pressed_keys)
                print(self.x, self.y)
        if (pressed_keys[K_RIGHT] or pressed_keys[K_d]):
            if self.x - 4 > -600:
                self.x -= 4
                print(self.x, self.y)
            else:
                self.x = -(self.bottom.get_width() - WIN_WIDTH)
                player.move(pressed_keys)
                print(self.x, self.y)
