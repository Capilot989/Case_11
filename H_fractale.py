import turtle as t


t.colormode(255)

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


def draw_line(pos1: list, pos2: list) -> None:
    """
    Draw a straight line between two points.

    Args:
        pos1 (list): Starting position as [x, y] coordinates
        pos2 (list): Ending position as [x, y] coordinates

    Return:
        None
    """
    t.penup()
    t.goto(pos1[0], pos1[1])
    t.pendown()
    t.goto(pos2[0], pos2[1])


def draw_H(x: float, y: float, width: float, height: float) -> None:
    """
    Draw a single H-shape at the specified position and size.

     Args:
         x (float): X-coordinate of the H's origin y (float):
         Y-coordinate of the H's origin
         width (float): Width of the H shape
         height (float): Height of the H shape

    Return:
        None
    """
    global step, total_steps
    t.pencolor(get_color(step, total_steps))
    step += 1

    draw_line([x + width * 0.25, y + height * 0.5],
              [x + width * 0.75, y + height * 0.5])
    draw_line([x + width * 0.25, y + height * 0.25],
              [x + width * 0.25, y + height * 0.75])
    draw_line([x + width * 0.75, y + height * 0.25],
              [x + width * 0.75, y + height * 0.75])


def H_recursive(
        x: float, y: float, 
        width: float, height: float, depth: int
) -> None:
    """
    Recursively draw H-fractal pattern.
    This function draws an H-shape and recursively calls itself for four quadrants around the H's endpoints.

    Args:
        x (float): X-coordinate of the current section's origin
        y (float): Y-coordinate of the current section's origin
        width (float): Width of the current drawing section
        height (float): Height of the current drawing section
        depth (int): Current recursion depth (stops when depth == 0)

    Return:
        None
    """
    if depth == 0:
        return

    draw_H(x, y, width, height)

    new_width = width / 2
    new_height = height / 2
    new_depth = depth - 1

    H_recursive(x, y + height / 2, new_width, new_height, new_depth)
    H_recursive(x + width / 2, y + height / 2, new_width, new_height, new_depth)
    H_recursive(x, y, new_width, new_height, new_depth)
    H_recursive(x + width / 2, y, new_width, new_height, new_depth)


def count_H_segments(depth: int) -> int:
    """
       Calculate the total number of H-shapes in the H-fractal.

       The H-fractal follows a pattern where each H-shape generates 4 smaller
       H-shapes at the next recursion level, resulting in exponential growth.

       Args:
           depth (int): Maximum recursion depth of the fractal

       Returns:
           int: Total number of H-shapes (1 + 4 + 16 + ... + 4^(depth-1))
       """
    if depth == 0:
        return 0
    return 1 + count_H_segments(depth - 1) * 4
