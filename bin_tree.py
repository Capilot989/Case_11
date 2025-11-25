import turtle as t

t.tracer(0)
t.left(90)
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
    Calculate the total number of segments in the binary tree fractal.

    The tree follows a pattern where each node creates 2 child segments,
    resulting in a geometric progression of segments.

    Args:
        depth (int): Recursion depth of the tree (0 means no segments)

    Return:
        int: Total number of line segments in the tree
    """
    if depth == 0:
        return 0
    return 1 + count_segments(depth - 1) * 2


def tree(length: int, depth: int, total: int) -> None:
    """
    Recursively draw a binary tree fractal with color gradient.

    The tree grows upward with branches splitting at 30° angles,
    creating a symmetrical binary branching pattern.

    Args:
        length (float): Length of the current branch segment
        depth (int): Current recursion depth (0 stops recursion)
        total (int): Total segments for color gradient calculation

    Return:
        None
    """
    global step
    if depth == 0:
        return

    t.pencolor(get_color(step, total))
    step += 1

    t.forward(length)
    t.right(30)
    tree(length * 0.6, depth - 1, total)
    t.left(60)
    tree(length * 0.6, depth - 1, total)
    t.right(30)
    t.backward(length)
