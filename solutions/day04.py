class Day04:
    def __init__(self, input):
        self.grid = Grid(str.splitlines(input))

    def part1_solution(self):
        return XMAS_Counter.count(self.grid.rows + self.grid.columns + self.grid.diagonals)

    def part2_solution(self):
        return XMAS_X_Counter.count(self.grid.diagonals)

class Grid:
    def __init__(self, lines):
        self.rows = []
        self.columns = []
        self.diagonals = []
        self.data = self.__populate(lines)

    def __populate(self, lines):
        grid = [[] for _ in range(len(lines))]
        for x, line in enumerate(lines):
            for y, char in enumerate(line):
                grid[x].append(Cell(char, x, y))

        max_cols = len(grid[0])
        max_rows = len(grid)

        forward_diag = [[] for _ in range(max_rows + max_cols - 1)]
        backward_diag = [[] for _ in range(len(forward_diag))]
        min_backward_diag = -max_rows + 1

        columns = [[] for _ in range(max_cols)]
        rows = [[] for _ in range(max_rows)]

        for x in range(max_cols):
            for y in range(max_rows):
                columns[x].append(grid[y][x])
                rows[y].append(grid[y][x])
                forward_diag[x+y].append(grid[y][x])
                backward_diag[x-y-min_backward_diag].append(grid[y][x])

        self.rows = rows
        self.columns = columns
        for line in forward_diag:
            self.diagonals.append(line)
        for line in backward_diag:
            self.diagonals.append(line)

        return grid

class Cell:
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.value} x{self.x} y{self.y}"
    
    def __repr__(self):
        return f"{self.value} x{self.x} y{self.y}"

class LineReader:
    @staticmethod
    def read(values):
        return "".join([i.value for i in values])

class XMAS_Counter:
    @staticmethod
    def count(input):
        count = 0

        for line in input:
            line_str = LineReader.read(line)
            count += line_str.count("XMAS") + line_str.count("SAMX")

        return count

class XMAS_X_Counter:
    @staticmethod
    def count(input):
        a_coords = {}

        lines = [x for x in input if len(x) >= 3]

        for line in lines:
            for i, char in enumerate(line):
                if char.value == "A" and i != 0 and i != len(line) - 1:
                    prev = line[i - 1]
                    next = line[i + 1]
                    if (prev.value == "M" and next.value == "S") or (prev.value == "S" and next.value == "M"):
                        if f"{char.x},{char.y}" in a_coords:
                            a_coords[f"{char.x},{char.y}"] += 1
                        else:
                            a_coords[f"{char.x},{char.y}"] = 1

        return len([x for x in a_coords.values() if x == 2])
