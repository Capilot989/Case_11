import turtle


turtle.colormode(255)

step = 0

def get_color(step: int, total: int) -> tuple:
    """
       Generate a smooth color transition from blue to red.

       Creates a linear gradient where blue intensity decreases and red intensity
       increases proportionally based on the current step in the total progression.

       Args:
           step (int): Current position in the color transition sequence
           total (int): Total number of steps for complete color transition

       Returns:
           tuple: RGB color as (red, green, blue) with values 0-255
       """
    r = int(255 * (step / total))
    g = 0
    b = int(255 * (1 - step / total))
    return (r, g, b)

def count_squares(level: int) -> int:
    """
       Calculate the total number of squares in the Sierpinski carpet fractal.

       The Sierpinski carpet follows a recursive pattern where each level creates
       8 smaller carpets around a central empty square, plus the current square.

       Args:
           level (int): Recursion depth of the fractal

       Returns:
           int: Total number of squares drawn (8 * previous + 1)
       """
    if level == 0:
        return 0
    return 8 * count_squares(level - 1) + 1

def draw_square(x: float, y: float, size: int, total: int) -> None:
    """
    Draw a square at the specified position and size.

    Args:
        x (float): X-coordinate of the bottom-left corner
        y (float): Y-coordinate of the bottom-left corner
        size (float): Side length of the square

    Return:
        None
    """
    global step
    turtle.pencolor(get_color(step, total))
    step += 1
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(0)
    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)

def sierpinski_carpet(
        x: float, y: float,
        size: int, level: int, total: int
) -> None:
    """
    Recursively draw the Sierpinski carpet fractal.

    The Sierpinski carpet is a fractal pattern created by recursively
    dividing a square into 9 smaller squares and removing the center one.

    Args:
        x (float): X-coordinate of the bottom-left corner
        y (float): Y-coordinate of the bottom-left corner
        size (float): Side length of the current square
        level (int): Current recursion depth (0 = draw nothing)

    Return:
        None
    """
    if level == 0:
        return

    draw_square(x, y, size, total)

    new_size = size / 3
    positions = [
        (x, y),
        (x + new_size, y),
        (x + 2*new_size, y),
        (x, y + new_size),
        (x + 2*new_size, y + new_size),
        (x, y + 2*new_size),
        (x + new_size, y + 2*new_size),
        (x + 2*new_size, y + 2*new_size),
    ]

    for nx, ny in positions:
        sierpinski_carpet(nx, ny, new_size, level - 1, total)
