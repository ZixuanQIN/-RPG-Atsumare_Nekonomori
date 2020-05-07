# _*_ coding: utf-8 _*_

import pygame
from pygame.locals import *

class Sprite:
    @staticmethod
    def draw(dest, source, x, y, cell_x, cell_y, cell_w=31, cell_h=31):
        """
        绘制精灵图中，指定x,y的图像
        :param dest: surface类型，要绘制到的目标surface
        :param source: surface类型，来源surface
        :param x: 绘制图像在dest中的坐标
        :param y: 绘制图像在dest中的坐标
        :param cell_x: 在精灵图中的格子坐标
        :param cell_y: 在精灵图中的格子坐标
        :param cell_w: 单个精灵的宽度
        :param cell_h: 单个精灵的高度
        :return:
        """
        dest.blit(source, (x, y), (cell_x * cell_w, cell_y * cell_h, cell_w, cell_h))

class CharWalk:
    DIR_DOWN = 0
    DIR_LEFT = 1
    DIR_RIGHT = 2
    DIR_UP = 3
 
    def __init__(self, hero_surf, char_id, dir, mx, my):
        """
        :param hero_surf: 精灵图的surface
        :param char_id: 角色id
        :param dir: 角色方向
        """
        self.hero_surf = hero_surf
        self.char_id = char_id
        self.dir = dir

        self.px = 4
 
        self.frame = 1  # 角色当前帧
        self.x = mx * self.px # 角色相对于地图的坐标
        self.y = my * self.px
        # 步长
        self.step = 0.5  # 每帧移动的像素
 
    def draw(self, screen_surf):
        # cell_x = self.char_id % 15 + int(self.frame)
        # cell_y = self.char_id // 16 + self.dir
        Sprite.draw(screen_surf, self.hero_surf, self.x, self.y, self.char_id, 0)
 
    # def goto(self, x, y):
    #     """
    #     :param x: 目标点
    #     :param y: 目标点
    #     """
    #     self.next_mx = x
    #     self.next_my = y
 
    #     # 设置人物面向
    #     if self.next_mx > self.mx:
    #         self.dir = CharWalk.DIR_RIGHT
    #     elif self.next_mx < self.mx:
    #         self.dir = CharWalk.DIR_LEFT
 
    #     if self.next_my > self.my:
    #         self.dir = CharWalk.DIR_DOWN
    #     elif self.next_my < self.my:
    #         self.dir = CharWalk.DIR_UP
 
    #     self.is_walking = True
 
    def move(self, pressed_keys):
        if (pressed_keys[K_UP] or pressed_keys[K_w]):
            t = self.y - int(self.px)
            if t >= 0:
                self.y = t
        if (pressed_keys[K_DOWN] or pressed_keys[K_s]):
            t = self.y + int(self.px)
            if t <= 440:
                self.y = t
        if (pressed_keys[K_LEFT] or pressed_keys[K_a]):
            t = self.x - int(self.px)
            if t >= 0:
                self.x = t
        if (pressed_keys[K_RIGHT] or pressed_keys[K_d]):
            t = self.x + int(self.px)
            if t <= 1248:
                self.x = t