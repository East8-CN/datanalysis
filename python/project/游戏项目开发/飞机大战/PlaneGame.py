# import pygame

class PlaneGame():
    def __init__(self):
        print("游戏初始化...")
        # 1.游戏初始化
        self.screen = pygame.display.set_mode()
        # 2.设置时钟
        self.clock = pygame.time.Clock()
        # 3.创建精灵对象 和 精灵组
        self.__create_spirites__()
    def __create_spirites__(self):
        print("创建精灵对象 与 精灵组...")
        pass

    def start_game(self):
        print("开始游戏...")


if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()
