import pyxel
from CasseBriques import CasseBriques

BALL_COLOR = 7
BALL_RADIUS = 3
SPEED = 5
NB_COLONNE = 10
NB_LIGNES = 3
SOLIDITE = 3
ESPACEMENT = 0
BRICK_WIDTH = 50
BRICK_HEIGHT = 25
WIDTH = (BRICK_WIDTH + ESPACEMENT) * NB_COLONNE
HEIGHT = 512
RACKET_Y = 450
RACKET_SPEED = 10
RACKET_WIDTH = 80
ANGLE_MIN = 10


class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT)
        # pyxel.load("my_resource.pyxres")
        self.casse_briques = CasseBriques()
        for ligne in range(2, 6):
            self.casse_briques.construire_rangee_briques(BRICK_WIDTH, BRICK_HEIGHT, 4, 10, NB_COLONNE, ESPACEMENT, ligne)

        self.derniere_brique_touchee = None

        self.ball_x = WIDTH//2
        self.ball_y = HEIGHT//2
        self.ball_vx = 0
        self.ball_vy = SPEED
        self.ball_r = BALL_RADIUS

        self.perdu = False

        self.racket_x = WIDTH//2


        pyxel.run(self.update, self.draw)

    def update(self):
        if self.perdu and pyxel.btnp(pyxel.KEY_SPACE):
            self.perdu = False
            self.ball_x = WIDTH//2
            self.ball_y = HEIGHT//2
            self.ball_vx = 0
            self.ball_vy = SPEED
            self.casse_briques = CasseBriques()
            
            for ligne in range(2, 6):
                self.casse_briques.construire_rangee_briques(BRICK_WIDTH, BRICK_HEIGHT, 4, 10, NB_COLONNE, ESPACEMENT, ligne)

            

        if pyxel.btn(pyxel.KEY_LEFT):
            self.racket_x = max(self.racket_x - RACKET_SPEED, 0)
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.racket_x = min(self.racket_x + RACKET_SPEED, WIDTH - RACKET_WIDTH)


        previous_x, previous_y = self.ball_x, self.ball_y
        self.ball_x += self.ball_vx
        self.ball_y += self.ball_vy
        if self.ball_x - self.ball_r <= 0 or self.ball_x + self.ball_r >= WIDTH:
            self.ball_vx *= -1
        if self.ball_y - self.ball_r <= 0:
            self.ball_vy *= -1

        if self.ball_y > HEIGHT:
            self.perdu = True

        brique_touchee = self.casse_briques.impact_brique(self.ball_x, self.ball_y)
        if brique_touchee != None:
            x1, y1, x2, y2 = brique_touchee.get_limits()
            if y1 <= previous_y <= y2 :
                self.ball_vx *= -1
            else:
                self.ball_vy *= -1

        if previous_y < RACKET_Y and self.ball_y >= RACKET_Y and self.racket_x <= self.ball_x <= self.racket_x + RACKET_WIDTH:
            angle = ANGLE_MIN + (self.ball_x - self.racket_x) / RACKET_WIDTH * (180 - 2 * ANGLE_MIN)
            self.ball_vx = - SPEED * pyxel.cos(angle)
            self.ball_vy = - SPEED * pyxel.sin(angle)


    def draw(self):
        pyxel.cls(0)
        pyxel.circ(self.ball_x, self.ball_y, self.ball_r, BALL_COLOR)
        for b in self.casse_briques.briques:
            x1, y1, x2, y2 = b.get_limits()
            pyxel.rect(x1+2, y1+2, x2-x1-4, y2-y1-4, 12 - b.solidite)
        pyxel.rect(self.racket_x, RACKET_Y, RACKET_WIDTH, 10, 12)

        if self.perdu:
            pyxel.text(WIDTH//2, HEIGHT//2, "PERDU", 7)


    
    
App()