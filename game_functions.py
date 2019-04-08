#!/usr/bin/env python
# Author:Wang Xueming
import sys
import pygame


def check_events(ship):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # 按键按下的事件
        elif event.type == pygame.KEYDOWN:
            # 右键
            if event.key == pygame.K_RIGHT:
                # 向右移动飞船
                ship.rect.centerx += 1


def update_screen(ai_settings, screen, ship):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()
