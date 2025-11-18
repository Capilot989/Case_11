import turtle as t


def square(size: int) -> None:
    """
        Draw a square with the given side length.

        Args:
            t: Turtle object to draw with
            size (float): Length of each side of the square
        """
    for _ in range(4):
        t.forward(size)
        t.right(90)


def fractal(size: int, angle: int, k: float, depth: int) -> None:
    """
        Draw a recursive fractal pattern of squares.

        The function draws a square and then recursively draws smaller squares
        at specified angles and distances, creating a spiral fractal pattern.

        Args:
            t: Turtle object to draw with
            size (float): Initial size of the square
            angle (float): Angle to turn after each square
            k (float): Scaling factor for positioning and size reduction (0 < k < 1)
            depth (int): Recursion depth (number of recursive calls)

        Returns:
            None: Function works by side effects (drawing)
        """
    if depth == 0:
        return

    square(size)
    t.penup()
    t.right(angle)
    t.forward(size * k)
    t.pendown()

    fractal(size * (1 - k), angle, k, depth - 1)
