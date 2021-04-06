import pygame as pg
from settings import *
from sprites import *
import sys


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.load_data()

    def load_data(self):
        self.playing = True
        self.paused = False
        self.ant_image = pg.image.load('ant.png').convert_alpha()
        self.crosshair_image = pg.image.load('cursor.png').convert_alpha()
        self.background = pg.image.load('ground.png').convert_alpha()

    def new_game(self):
        self.ant_home = pg.Rect((WIDTH/2, HEIGHT/2), (15, 15))
        self.ant_group = pg.sprite.Group()
        self.home_group = pg.sprite.Group()
        self.crosshair_group = pg.sprite.Group()
        self.ant = Ant(self, self.ant_home.center)
        self.ant_group.add(self.ant)
        self.crosshair = Crosshair(self)
        self.crosshair_group.add(self.crosshair)
        self.background_rect = self.background.get_rect()
        self.debug = False
        pg.mouse.set_visible(False)

    def run(self):
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            if not self.paused:
                self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        #handles the changes and collisions
        self.ant_group.update()
        self.crosshair_group.update()

    def draw(self):
        #draw the sprites after getting new changes
        pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        #self.screen.fill(WHITE)
        self.screen.blit(self.background, self.background_rect)
        pg.draw.rect(self.screen, BLACK, self.ant_home)
        self.ant_group.draw(self.screen)
        self.crosshair_group.draw(self.screen)

        if self.debug:
            pass
        pg.display.flip()

    def events(self):
        #get keypressed from player
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_p:
                    self.paused = not self.paused
                    print('Paused')
                if event.key == pg.K_TAB:
                    self.debug = not self.debug

    def main_menu(self):
        # this will draw the main menu for the game
        pass


g = Game()
g.new_game()
g.run()