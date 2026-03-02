from random import random, choice

class Grid:
    def __init__(self, size=4):
        self.size = size
        self.__g = [[0 for _ in range(size)] for _ in range(size)]
        # self.__g = [[i*size+j for i in range(size)] for j in range(size)]

    def __str__(self):
        s = ""
        for i in range(self.size):
            for j in range(self.size):
                s+=str(self.__g[i][j]) + " "
            s+="\n"
        return s
    
    def add_random(self):
        """
            adds new values to an empty slot (value = 0). if there is None, returns False
        """
        empty_coords = [(i, j) for i in range(self.size) for j in range(self.size) if self.__g[i][j] == 0]
        
        if len(empty_coords) == 0:
            return False
                
        coords = choice(empty_coords)
        if random() < 0.1:
            self.__g[coords[0]][coords[1]] = 2
        else:
            self.__g[coords[0]][coords[1]] = 1
        
        return True

    def get_value(self, x, y):
        return self.__g[y][x]

    def slide_left(self):
        return_value = False
        for line in self.__g:
            for j in range(self.size):
                if line[j] != 0:
                    k = j
                    v = line[j]
                    line[j] = 0
                    while k > 0 and line[k-1] == 0:
                        k-=1
                    line[k] = v
                    if k != j:
                        return_value = True
        return return_value

    def slide_right(self):
        return_value = False
        for line in self.__g:
            for j in range(self.size-1, -1, -1):
                if line[j] != 0:
                    k = j
                    v = line[j]
                    line[j] = 0
                    while k < self.size-1 and line[k+1] == 0:
                        k+=1
                    line[k] = v
                    if k != j:
                        return_value = True
        return return_value

    def slide_up(self):
        return_value = False
        for j in range(self.size):
            for i in range(self.size):
                if self.__g[i][j] != 0:
                    k = i
                    v = self.__g[i][j]
                    self.__g[i][j] = 0
                    while k > 0 and self.__g[k-1][j] == 0:
                        k-=1
                    self.__g[k][j] = v
                    if k != i:
                        return_value = True

        return return_value

    def slide_down(self):
        return_value = False
        for j in range(self.size):
            for i in range(self.size-1, -1, -1):
                if self.__g[i][j] != 0:
                    k = i
                    v = self.__g[i][j]
                    self.__g[i][j] = 0
                    while k < self.size-1 and self.__g[k+1][j] == 0:
                        k+=1
                    self.__g[k][j] = v
                    if k != i:
                        return_value = True

        return return_value

    def combine_left(self):
        return_value = False
        for line in self.__g:
            for j in range(self.size-1):
                if line[j+1]==line[j] and line[j] != 0:
                    line[j] += 1
                    line[j+1] = 0
                    return_value = True
        return return_value

    def combine_right(self):
        return_value = False
        for line in self.__g:
            for j in range(self.size-1, 0, -1):
                if line[j-1]==line[j] and line[j] != 0:
                    line[j] += 1
                    line[j-1] = 0
                    return_value = True
        return return_value

    def combine_up(self):
        return_value = False
        for j in range(self.size):
            for i in range(self.size-1):
                if self.__g[i+1][j]==self.__g[i][j] and self.__g[i][j] != 0:
                    self.__g[i][j] += 1
                    self.__g[i+1][j] = 0
                    return_value = True
        return return_value

    def combine_down(self):
        return_value = False
        for j in range(self.size):
            for i in range(self.size-1, 0, -1):
                if self.__g[i-1][j]==self.__g[i][j] and self.__g[i][j] != 0:
                    self.__g[i][j] += 1
                    self.__g[i-1][j] = 0
                    return_value = True
        return return_value


