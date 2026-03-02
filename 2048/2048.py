import pyxel
from grid import Grid

GRID_SIZE = 4
CELL_SIZE = 16
WIDTH = GRID_SIZE * CELL_SIZE + 1
HEIGHT = GRID_SIZE * CELL_SIZE + 1


class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT)
        pyxel.load("my_resource_2.pyxres")
        self.grid = Grid(GRID_SIZE)
        self.grid.add_random()

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_LEFT):
            slide = self.grid.slide_left()
            combine = self.grid.combine_left()
            if slide or combine:
                self.grid.slide_left()
                self.grid.add_random()

        if pyxel.btnp(pyxel.KEY_RIGHT):
            slide = self.grid.slide_right()
            combine = self.grid.combine_right()
            if slide or combine:
                self.grid.slide_right()
                self.grid.add_random()

        if pyxel.btnp(pyxel.KEY_UP):
            slide = self.grid.slide_up()
            combine = self.grid.combine_up()
            if slide or combine:
                self.grid.slide_up()
                self.grid.add_random()
                
        if pyxel.btnp(pyxel.KEY_DOWN):
            slide = self.grid.slide_down()
            combine = self.grid.combine_down()
            if slide or combine:
                self.grid.slide_down()
                self.grid.add_random()
                


    def draw(self):
        pyxel.cls(13)
        
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                v = self.grid.get_value(x, y)
                if v!=0:
                    pyxel.blt(x*CELL_SIZE, y*CELL_SIZE, 0, 0, (v-1) * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        

App()