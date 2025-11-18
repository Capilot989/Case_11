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

def count_segments(rec_num: int) -> int:
    """
       Calculate the total number of base segments in the ice fractal.

       The ice fractal follows a pattern where each recursion level multiplies
       the number of segments by 4, resulting in exponential growth.

       Args:
           rec_num (int): Recursion depth of the fractal

       Returns:
           int: Total number of base drawing segments (4^rec_num)
       """
    if rec_num == 0:
        return 1
    return count_segments(rec_num - 1) * 4

def ice_fract(rec_num: int, size: float, total: int) -> None:
    """
       Draw an ice fractal using recursion.

       This function recursively draws a fractal pattern that resembles ice crystals
       or snowflakes by repeatedly dividing the line segments and adding perpendicular branches.

       Args:
           rec_num (int): The recursion depth
           size (float): The size of the fractal segment

       Return:
           None
       """
    global step
    if rec_num == 0:
        turtle.pencolor(get_color(step, total))
        step += 1

        turtle.forward(size/2)
        turtle.left(90)
        turtle.forward(size/3)

        turtle.back(size/3)
        turtle.right(90)
        turtle.forward(size/2)
    else:
        ice_fract(rec_num-1, size/4, total)
        turtle.left(90)
        ice_fract(rec_num-1, size/6, total)
        turtle.right(180)
        ice_fract(rec_num-1, size/6, total)
        turtle.left(90)
        ice_fract(rec_num-1, size/4, total)
