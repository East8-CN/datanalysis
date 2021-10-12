# import pygame
# 定义飞机大战游戏精灵父类GameSprite
# 实现英雄飞机可以在垂直方向上按照一定速度移动
# 调用初始化方法__init__封装属性图片名称imageName 图片位置imageRect 移动速度speed
# 如果类中没有继承object主类,则在初始化方法中首先调用父类的初始化方法,否则不能使用父类的方法
# 定义update方法更新图片坐标
#
#
# 如果父类的方法中不能满足要求,则派生出一个子类
# class BackGround  初始化方法中添加属性is_alt(默认值是false)是否是替换背景图片 如果是的话就设置图片的位置 设置图片的位置为-self.rect.height
# 调用update方法  判断是否移除屏幕  当移出屏幕时,就将另一张图片设置到屏幕上方
