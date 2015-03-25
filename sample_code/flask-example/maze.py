"""Maze module for demo purposes"""
EAST = (1, 0)
NORTH = (1, 1)
WEST = (0, 1)
SOUTH = (0, 0)


def generate(width=100, height=60):
    """Generates a maze with `width` and `height`

    :param width: Integer for the width (default 100)
    :param height: Integer for the height (default 60)

    Returns a Maze. This will be an instance of either :class:`KruskalMaze`
    or :class:`RecursiveMaze`, depending on which algorithm you chose to
    generate it with.
    """
    pass


class Maze:
    """The Maze class"""
    def run(self):
        """Runs the maze"""
        pass


class KruskalMaze(Maze):
    """The Kruskal Maze class"""
    def run(self):
        """Runs the maze"""
        pass


class RecursiveMaze(Maze):
    """The Kruskal Maze class"""
    def run(self):
        """Runs the maze"""
        pass


class Kruskal:
    """Kruskal algorithm for generating mazes"""
    def create():
        """Creates a maze"""
        return KruskalMaze()


class Recursive:
    """Recursive algorithm for generating mazes"""
    def create():
        """Creates a maze"""
        return RecursiveMaze()


def run():
    """Runs the maze"""
    pass
