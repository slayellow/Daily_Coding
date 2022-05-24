

class Boundaries:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def __contain__(self, coord):
        x, y = coord
        return 0 <= x < self.width and 0 <= y < self.height


class Grid:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.limits = Boundaries(width, height)

    def __contain__(self, coord):
        return coord in self.limits
