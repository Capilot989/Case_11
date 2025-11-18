import turtle

turtle.colormode(255)
turtle.tracer(0)

step = 0

def get_color(step: int, total: int) -> tuple:
    """
        Generate a smooth color transition from blue to red with safe value clamping.

        Creates a linear gradient where blue intensity decreases and red intensity
        increases proportionally, with values clamped to the valid 0-255 range
        to prevent out-of-bounds color values.

        Args:
            step (int): Current position in the color transition sequence
            total (int): Total number of steps for complete color transition

        Returns:
            tuple: RGB color as (red, green, blue) with values safely clamped to 0-255
        """
    r = min(255, max(0, int(255 * step / total)))
    g = 0
    b = min(255, max(0, int(255 * (1 - step / total))))
    return (r, g, b)

def count_branches(n: int) -> int:
    """
    Calculate the total number of branch segments in the fractal tree.

    The fractal tree follows a complex branching pattern where each branch
    at depth n creates multiple sub-branches of decreasing depths, with
    the branching factor varying at each level.

    Args:
        n (int): Maximum recursion depth of the tree

    Returns:
        int: Total number of branch segments and leaves
    """
    if n == 0:
        return 1
    total = 0
    for i in range(n):
        total += count_branches(n - i - 1) * 2
    return total + 1

def branch(n: int, size: float, total: int) -> None:
    """
        Recursively draw a fractal tree pattern.

        This function creates a branching fractal pattern where each branch
        splits into two smaller branches at 45-degree angles.

        Args:
            n (int): Current recursion depth (0 = draw leaf)
            size (float): Length of the current branch

        Return:
            None
        """
    global step
    if n == 0:
        turtle.forward(size)
        step += 1
        turtle.pencolor(get_color(step, total))
        turtle.backward(size)
        return

    x = size / (n + 1)

    for i in range(n):
        turtle.forward(x)
        step += 1
        turtle.pencolor(get_color(step, total))

        turtle.left(45)
        branch(n - i - 1, 0.5 * x * (n - i - 1), total)

        turtle.left(90)
        branch(n - i - 1, 0.5 * x * (n - i - 1), total)
        turtle.right(135)

    turtle.forward(x)
    step += 1
    turtle.pencolor(get_color(step, total))
    turtle.left(180)
    turtle.forward(size)
