from src import *
import src.Settings as Settings
from src.Cell import *
from src.Position import *

class Grid:

    def __init__(self):

        self.size = (Settings.COLLNO, Settings.ROWNO)
        self.cells = [[0 for x in range(self.size[1])] for y in range(self.size[0])]
        self.next_state = [[0 for x in range(self.size[1])] for y in range(self.size[0])]

        for i in range(self.size[0]):
            for j in range(self.size[1]):
                self.cells[i][j] = Cell(Position(i, j))

    def update(self):
        self.__generate_next_step()
        self.__set_next_state()

    def __generate_next_step(self):
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                living = self.cells[i][j].is_alive
                count = self.get_living_neighbours(i, j)
                result = False

                if living and count < 2:
                    result = False
                if living and (count == 2 or count == 3):
                    result = True
                if living and count > 3:
                    result = False
                if not living and count == 3:
                    result = True

                self.next_state[i][j] = result

    def __set_next_state(self):
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                self.cells[i][j].is_alive = self.next_state[i][j]

    def get_living_neighbours(self, x, y):

        count = 0

        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if self.get_cell(x + i, y + j).is_alive:
                    count += 1

        return count

    def render(self, screen):

        for i in range(self.size[0]):
            for j in range(self.size[1]):
                self.cells[i][j].draw(screen)

    def get_cell(self, i, j):
        if i == -1:
            x = Settings.COLLNO - 1
        elif i == Settings.COLLNO:
            x = 0
        else:
            x = i

        if j == -1:
            y = Settings.ROWNO - 1
        elif j == Settings.ROWNO:
            y = 0
        else :
            y = j

        return self.cells[x][y]