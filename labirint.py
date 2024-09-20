from random import choice

WALL = '█'
EMPTY = '░'

class Maze:
    def __init__(self, rows: int, cols: int) -> None:
        self.rows = rows
        self.cols = cols
        self.is_ready = False
        self.map = []
        self.make_walls()

    def make_walls(self) -> None:
        for i in range(self.rows):
            self.map.append([WALL] * self.cols)


    def show_map(self) -> None:
        for row in self.map:
            print(*row, sep='')


    def make_path(self) -> None:
        self.bulldozer_row = choice(range(2, self.rows, 2))
        self.bulldozer_col = choice(range(2, self.cols, 2))
        self.map[self.bulldozer_row][self.bulldozer_col] = EMPTY

        while not self.is_ready:
            all_directions = []
            if self.bulldozer_col < self.cols - 2:
                all_directions.append('right')
            if self.bulldozer_col > 0:
                all_directions.append('left')
            if self.bulldozer_row > 0:
                all_directions.append('up')
            if self.bulldozer_row < self.rows - 2:
                all_directions.append('down')

            direction = choice(all_directions)


            if direction == 'right':
                if self.map[self.bulldozer_row][self.bulldozer_col + 2] == WALL:
                    self.map[self.bulldozer_row][self.bulldozer_col + 1] = EMPTY
                    self.map[self.bulldozer_row][self.bulldozer_col + 2] = EMPTY
                self.bulldozer_col += 2
            elif direction == 'left':
                if self.map[self.bulldozer_row][self.bulldozer_col - 2] == WALL:
                    self.map[self.bulldozer_row][self.bulldozer_col - 1] = EMPTY
                    self.map[self.bulldozer_row][self.bulldozer_col - 2] = EMPTY
                self.bulldozer_col -= 2
            elif direction == 'up':
                if self.map[self.bulldozer_row - 2][self.bulldozer_col] == WALL:
                    self.map[self.bulldozer_row - 1][self.bulldozer_col] = EMPTY
                    self.map[self.bulldozer_row - 2][self.bulldozer_col] = EMPTY
                self.bulldozer_row -= 2
            elif direction == 'down':
                if self.map[self.bulldozer_row + 2][self.bulldozer_col] == WALL:
                    self.map[self.bulldozer_row + 1][self.bulldozer_col] = EMPTY
                    self.map[self.bulldozer_row + 2][self.bulldozer_col] = EMPTY
                self.bulldozer_row += 2

            for i in self.map:
                if i // 2 == EMPTY:
                    break


maze = Maze(15, 11)
maze.make_path()
maze.show_map()



