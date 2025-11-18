import turtle as t

t.colormode(255)

step = 0


def get_color(step: int, total_steps: int) -> tuple:
    """
    Generate a smooth color transition from blue to red.

    The color transitions linearly from pure blue (0,0,255) at step 0
    to pure red (255,0,0) at the final step.

    Args:
        step (int): Current step in the color transition (0 to total_steps)
        total_steps (int): Total number of steps in the transition

    Returns:
        tuple: RGB color as (r, g, b) tuple with values 0-255
    """
    r = int(255 * (step / total_steps))
    g = 0
    b = int(255 * (1 - step / total_steps))
    return (r, g, b)


def count_segments(depth: int) -> int:
    """
    Calculate the number of base segments in a Levy curve for given depth.

    The Levy curve doubles the number of segments with each recursion level.

    Args:
        depth (int): Recursion depth of the Lévy C curve

    Returns:
        int: Total number of line segments in the curve (2^depth)
    """
    return 2 ** depth


def levi(length: int, depth: int, total_steps: int) -> None:
    """
       Recursively draw the Levy fractal curve with color gradient.

       The Levy curve is constructed by replacing straight lines with
       two perpendicular segments forming a right angle at each recursion.

       Args:
           length (float): Current segment length
           depth (int): Current recursion depth (0 draws straight line)
           total_steps (int): Total segments for color gradient calculation
       """
    global step

    if depth == 0:
        t.pencolor(get_color(step, total_steps))
        step += 1
        t.forward(length)
    else:
        t.left(45)
        levi(length / 2 ** 0.5, depth - 1, total_steps)
        t.right(90)
        levi(length / 2 ** 0.5, depth - 1, total_steps)
        t.left(45)
