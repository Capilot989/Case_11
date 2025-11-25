import turtle as t

t.colormode(255)

step = 0
t.right(90)


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


def count_segments(depth: int) -> int:
    """
    Calculate the number of segments in a Koch curve of given depth.

    The Koch curve quadruples the number of segments with each recursion level
    because each segment is replaced by 4 smaller segments.

    Args:
        depth (int): Recursion depth of the Koch curve

    Return:
        int: Total number of line segments (4^depth)
    """
    return 4 ** depth


def koch(size: float, depth: int, total: int) -> None:
    """
    Recursively draw a Koch curve segment with color gradient.

    The Koch curve replaces each straight line with a pattern of four segments
    that form a triangular bump, creating a fractal snowflake edge.

    Args:
        size (float): Length of the current segment
        depth (int): Current recursion depth (0 draws straight line)
        total (int): Total segments for color gradient calculation

    Return:
        None
    """
    global step

    if depth == 0:
        t.pencolor(get_color(step, total))
        step += 1
        t.forward(size)
        return

    koch(size / 3, depth - 1, total)
    t.left(60)

    koch(size / 3, depth - 1, total)
    t.right(120)

    koch(size / 3, depth - 1, total)
    t.left(60)

    koch(size / 3, depth - 1, total)


def snowflake(size: int, depth: int, total: int) -> None:
    """
    Draw a complete Koch snowflake by combining three Koch curves.

    The Koch snowflake is formed by arranging three Koch curves in an
    equilateral triangle pattern, creating a closed fractal shape.

    Args:
        size (int): Length of each side of the snowflake
        depth (int): Recursion depth for the Koch curves
        total (int): Total segments for color gradient in snowflake

    Return:
        None
    """
    for _ in range(3):
        koch(size, depth, total)
        t.right(120)
