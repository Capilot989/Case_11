import turtle as t


def square(size: int) -> None:
    """
    Draw a square with the given side length.

    Args:
        size (float): Length of each side of the square

    Return:
        None
    """
    for _ in range(4):
        t.forward(size)
        t.right(90)


def running_squere(size: int, angle: int, koef: float, depth: int) -> None:
    """
    Draw a recursive fractal pattern of squares.

    The function draws a square and then recursively draws smaller squares
    at specified angles and distances, creating a spiral fractal pattern.

    Args:
        size (float): Initial size of the square
        angle (float): Angle to turn after each square
        koef (float): Scaling factor for positioning and size reduction 
                        (0 < k < 1)
        depth (int): Recursion depth (number of recursive calls)

    Return:
        None
    """
    if depth == 0:
        return

    square(size)
    t.penup()
    t.right(angle)
    t.forward(size * koef)
    t.pendown()

    running_squere(size * (1 - koef), angle, koef, depth - 1)
