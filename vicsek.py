import turtle as t

t.colormode(255)
step = 0


def get_color(step: int, total: int) -> tuple:
    """
    Generate a smooth color transition from blue to red.

    Creates a linear gradient where blue 
    intensity decreases and red intensity increases
    proportionally based on the current step in the total progression.

    Args:
        step (int): Current position in the color transition sequence
        total (int): Total number of steps for complete color transition

    Return:
        tuple: RGB color as (red, green, blue) with values 0-255
    """
    red = int(255 * (step / total))
    green = 0
    blue = int(255 * (1 - step / total))

    return (red, green, blue)


def count_squares(depth: int) -> int:
    """
    Calculate the total number of squares in the Vicsek fractal.

    The Vicsek fractal follows a pattern where each recursion level
    multiplies the number of squares by 5 (center + 4 directional squares).

    Args:
        depth (int): Recursion depth of the fractal

    Returns:
        int: Total number of squares (5^depth)
    """
    return 5 ** depth


def draw_square(x: float, y: float, size: int, color: str) -> None:
    """
    Draw a single square at the specified position with given color.

    Args:
        x (float): X-coordinate of the bottom-left corner
        y (float): Y-coordinate of the bottom-left corner
        size (int): Side length of the square
        color (str): Color tuple or string for the square outline

    Return:
        None
    """
    t.pencolor(color)
    t.penup()
    t.goto(x, y)
    t.pendown()

    for _ in range(4):
        t.forward(size)
        t.left(90)


def vicsek(x: float, y: float, size: int, depth: int, total: int) -> None:
    """
    Recursively draw the Vicsek fractal (cross fractal) with color gradient.

    The Vicsek fractal divides a square into 9 smaller squares and draws
    only the center and four edge squares (forming a cross pattern).

    Args:
        x (float): X-coordinate of current square's bottom-left corner
        y (float): Y-coordinate of current square's bottom-left corner
        size (int): Side length of current square
        depth (int): Current recursion depth (0 draws single square)
        total (int): Total squares for color gradient calculation

    Return:
        None
    """
    global step

    if depth == 0:
        col = get_color(step, total)
        step += 1
        draw_square(x, y, size, col)
        return

    new_size = size / 3

    positions = [
        (x + new_size, y + new_size),
        (x, y + new_size),
        (x + 2 * new_size, y + new_size),
        (x + new_size, y),
        (x + new_size, y + 2 * new_size)
    ]

    for x, y in positions:
        vicsek(x, y, new_size, depth - 1, total)
