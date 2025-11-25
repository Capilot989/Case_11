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


def count_segments(depth: int) -> int:
    """
    Calculate the number of base segments in a Levy curve for given depth.

    The Levy curve doubles the number of segments with each recursion level.

    Args:
        depth (int): Recursion depth of the Lévy C curve

    Return:
        int: Total number of line segments in the curve (2^depth)
    """
    return 2 ** depth


def levi(length: int, depth: int, total: int) -> None:
    """
    Recursively draw the Levy fractal curve with color gradient.

    The Levy curve is constructed by replacing straight lines with
    two perpendicular segments forming a right angle at each recursion.

    Args:
        length (float): Current segment length
        depth (int): Current recursion depth (0 draws straight line)
        total_steps (int): Total segments for color gradient calculation

    Return:
        None
    """
    global step

    if depth == 0:
        t.pencolor(get_color(step, total))
        step += 1
        t.forward(length)
    else:
        t.left(45)
        levi(length / 2 ** 0.5, depth - 1, total)
        t.right(90)
        levi(length / 2 ** 0.5, depth - 1, total)
        t.left(45)
