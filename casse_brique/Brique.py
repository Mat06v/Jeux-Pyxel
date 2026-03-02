class Brique:
    def __init__(self, couleur, solidite, points, x_position, y_position, largeur, hauteur):
        self.couleur = couleur
        self.points = points
        self.solidite = solidite
        self.x_position, self.y_position = x_position, y_position
        self.largeur, self.hauteur = largeur, hauteur

    def __str__(self):
        return f"Couleur: {self.couleur}\nSolidité: {self.solidite}\nPoints: {self.points}\nCoordonées: {self.x_position}, {self.y_position}\nDimensions: {self.largeur}, {self.hauteur}"

    def get_limits(self):
        return (self.x_position, self.y_position, self.x_position + self.largeur, self.y_position + self.hauteur)
    
    def is_hit(self, ball_x, ball_y):
        limits = self.get_limits()
        if limits[0] <= ball_x <= limits[2] and limits[1] <= ball_y <= limits[3]:
            print("touché")
            self.solidite -= 1
            return self.points
        return 0

# b = Brique("red", 3, 10, 60, 20, 50, 25)
# print(b.is_hit(65, 25))