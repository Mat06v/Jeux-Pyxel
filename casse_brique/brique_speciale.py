from Brique import Brique

class BriqueSpeciale(Brique):
    def __init__(self, couleur, solidite, points, x_position, y_position, largeur, hauteur, effet_special):
        super().__init__(couleur, solidite, points, x_position, y_position, largeur, hauteur)
        self.effet = effet_special

    def is_hit(self, ball_x, ball_y):
        pts_gagnes = super().is_hit(ball_x, ball_y)
        if self.effet == "Double Score":
            return 2 * pts_gagnes
        return pts_gagnes
    
    def __str__(self):
        return super().__str__() + f"\nEffet: {self.effet}"

# b = BriqueSpeciale("red", 3, 10, 60, 20, 50, 25, "Double Score")
# print(b)