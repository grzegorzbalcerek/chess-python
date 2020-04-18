from enum import Enum

class Color(Enum):
    """
    The `Color` class represents one of the two colors (`Black` or `White`)
    used in the game of Chess.
    """
    WHITE = 1
    BLACK = 8

    def other(self):
        """
        Returns the opposite color.

        >>> Color.WHITE.other()
        <Color.BLACK: 8>
        >>> Color.BLACK.other()
        <Color.WHITE: 1>
        """
        if self == Color.WHITE:
            return Color.BLACK
        elif self == Color.BLACK:
            return Color.WHITE

    def first_row(self):
        """
        Returns the coordinate of the first row
        from the point of view of a player who plays the given color.

        >>> Color.WHITE.first_row()
        1
        >>> Color.BLACK.first_row()
        8
        """
        return self.value

if __name__ == "__main__":
    import doctest
    doctest.testmod()

