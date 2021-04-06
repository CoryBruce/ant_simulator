import pygame as pg
from settings import *

class Ant(pg.sprite.Sprite):
    def __init__(self, game, ant_home):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = game.ant_image.copy()
        self.rect = self.image.get_rect()
        self.hit_rect = self.rect.center
        self.marker_decay_time = 150000
        self.health = ANT_HEALTH
        self.pos = ant_home
        self.action = 'searching'
        self.searching_marker_list = []
        self.food_to_home_marker_list = []
        self.home_to_food_marker_list = []

    def update(self):
        # depending on self.action call methods below
        pass

    def search_for_food(self):
        # leave home in a random direction
        # leave a pheromone rect every 100px
        # add these rects to list
        # when within range of food item ant walks towards food
        # when ant touches food change self.action to got_food
        pass

    def take_food_home(self):
        # check food source for available food
            # if false set self.action = searching
            # self.search_for_food()
        # if true then split food image into small rects and have ant grab one
        # read the searching marker list and follow the closest rect
        # once ant hits that rect move from search list to food to home list, and check for next closest rect
        # move to next rect and repeat until home
        # when ant touches home drop food and self.action = 'home_to_food'
        pass

    def home_to_food(self):
        # read the food to home marker list and check the next closest rect
        # move to that rect and add a marker to the home to food list
        # repeat steps until get back to food source
        # check food source
            # if true: grab food and take_food_home()
            # if false: search_for_food()
        pass

    def check_food_source(self):
        # this reads the amount of food left
        # split up food into small rects so ants can take it away
        pass

    def check_other_markers(self):
        # this reads other ant markers
        # ignore the searching markers
        # prioritise food to home trails
        # go the other way from home on the trail
        pass

class Home(pg.sprite.Sprite):
    def __init__(self, game, pos_x, pos_y):
        super().__init__()
        self.game = game
        self.image = pg.Surface((15, 15))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    def update(self):
        pass

class Crosshair(pg.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = game.crosshair_image.copy()
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = pg.mouse.get_pos()

class Food(pg.sprite.Sprite):
    def __init__(self, game, pos_x, pos_y):
        super().__init__()
        self.game = game
        self.image = pg.Surface((50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.food_rect_list = []
        self.food_amount = FOOD_AMOUNT

    def update(self):
        pass

    def break_up_food(self):
        # this will take the rect and break it into smaller rects and add them to a list
        pass
