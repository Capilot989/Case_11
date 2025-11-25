import turtle

turtle.colormode(255)
turtle.tracer(0)

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
    t = max(0, min(step / total, 1))

    red = int(255 * t)
    green = 0
    blue = int(255 * (1 - t))

    return (red, green, blue)


def count_branches(depth: int) -> int:
    """
    Calculate the total number of branch segments in the fractal tree.

    The fractal tree follows a complex branching pattern where each branch
    at depth n creates multiple sub-branches of decreasing depths, with
    the branching factor varying at each level.

    Args:
        depth (int): Maximum recursion depth of the tree

    Return:
        int: Total number of branch segments and leaves
    """
    if depth == 0:
        return 1

    total = 0

    for i in range(depth):
        total += count_branches(depth - i - 1) * 2

    return total + 1


def branch(depth: int, size: float, total: int) -> None:
    """
    Recursively draw a fractal tree pattern.

    This function creates a branching fractal pattern where each branch
    splits into two smaller branches at 45-degree angles.

    Args:
        depth (int): Current recursion depth (0 = draw leaf)
        size (float): Length of the current branch

    Return:
        None
    """
    global step

    if depth == 0:
        turtle.forward(size)
        step += 1
        turtle.pencolor(get_color(step, total))
        turtle.backward(size)
        return

    x = size / (depth + 1)

    for i in range(depth):
        turtle.forward(x)
        step += 1
        turtle.pencolor(get_color(step, total))

        turtle.left(45)
        branch(depth - i - 1, 0.5 * x * (depth - i - 1), total)

        turtle.left(90)
        branch(depth - i - 1, 0.5 * x * (depth - i - 1), total)
        turtle.right(135)

    turtle.forward(x)
    step += 1
    turtle.pencolor(get_color(step, total))
    turtle.left(180)
    turtle.forward(size)
