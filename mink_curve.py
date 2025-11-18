import turtle

turtle.speed(0)
turtle.colormode(255)

step = 0


def get_color(step, total):
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


def count_segments(rec_num):
    """
       Calculate the total number of line segments in the Minkowski curve.

       The Minkowski curve follows a pattern where each recursion level multiplies
       the number of segments by 8, resulting in exponential growth.

       Args:
           rec_num (int): Recursion depth of the fractal

       Returns:
           int: Total number of line segments (8^rec_num)
       """
    if rec_num == 0:
        return 1
    return count_segments(rec_num - 1) * 8


def mink_curve(rec_num: int, size: float, total: int) -> None:
    """
        Draw the Minkowski curve fractal using recursion.

        This function recursively draws the Minkowski curve, a fractal pattern
        that fills a square area with a continuous but non-differentiable curve.

        Args:
            rec_num (int): The recursion depth
            size (float): The size of the fractal curve

        Return:
            None
        """
    global step
    if rec_num == 0:
        turtle.pencolor(get_color(step, total))
        step += 1
        turtle.forward(size)
    else:
        mink_curve(rec_num - 1, size / 4, total)
        turtle.left(90)
        mink_curve(rec_num - 1, size / 4, total)
        turtle.right(90)
        mink_curve(rec_num - 1, size / 4, total)
        turtle.right(90)
        mink_curve(rec_num - 1, size / 4, total)

        mink_curve(rec_num - 1, size / 4, total)
        turtle.left(90)
        mink_curve(rec_num - 1, size / 4, total)
        turtle.left(90)
        mink_curve(rec_num - 1, size / 4, total)
        turtle.right(90)
        mink_curve(rec_num - 1, size / 4, total)
