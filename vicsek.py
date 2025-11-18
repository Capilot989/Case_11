import turtle as t


def draw_square(x: float, y: float, size: int):
    """
       Draw a square at the specified position with given size.

       Args:
           x (float): X-coordinate of the bottom-left corner of the square
           y (float): Y-coordinate of the bottom-left corner of the square
           size (float): Side length of the square
       """
    t.penup()
    t.goto(x, y)
    t.pendown()
    for _ in range(4):
        t.forward(size)
        t.left(90)


def vicsek(x: float, y: float, size: int, depth: int) -> None:
    """
    Recursively draw the Vicsek fractal (cross fractal).

    The Vicsek fractal is created by dividing a square into 9 smaller squares
    and drawing only the center and four edge squares at each recursion level.

    Args:
        x (float): X-coordinate of the bottom-left corner of the current square
        y (float): Y-coordinate of the bottom-left corner of the current square
        size (float): Side length of the current square
        depth (int): Recursion depth (0 draws a single square.
    """
    if depth == 0:
        draw_square(t, x, y, size)
        return

    new_size = size / 3
    positions = [
        (x + new_size, y + new_size),  # центр
        (x, y + new_size),  # левый
        (x + 2 * new_size, y + new_size),  # правый
        (x + new_size, y),  # нижний
        (x + new_size, y + 2 * new_size)  # верхний
    ]

    for px, py in positions:
        vicsek(t, px, py, new_size, depth - 1)
