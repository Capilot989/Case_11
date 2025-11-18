import turtle as t

t.colormode(255)
t.tracer(0)

step = 0


def get_color(step: int, total: int) -> tuple:
    """
        Generate a smooth color transition from blue to red.

        Creates a gradient where colors transition from pure blue (0,0,255)
        to pure red (255,0,0) based on the current progress.

        Args:
            step (int): Current step in the color progression
            total (int): Total number of steps for complete transition

        Returns:
            tuple: RGB color tuple (r, g, b) with values 0-255
        """
    r = int(255 * (step / total))
    g = 0
    b = int(255 * (1 - step / total))
    return (r, g, b)


def count_segments(depth: int) -> int:
    """
      Calculate the total number of segments in the ice fractal.

      Uses recursive formula where each level multiplies the previous
      segment count by 6.

      Args:
          depth (int): Recursion depth of the fractal

      Returns:
          int: Total number of line segments at given depth
      """
    if depth == 0:
        return 1
    return 6 * count_segments(depth - 1)


def ice_fract_2(depth: int, size: float, total: int) -> None:
    """
    Recursively draw an ice crystal fractal with color gradient.
    
    This fractal creates a symmetrical ice-like pattern by recursively
    dividing segments and rotating at specific angles to form crystalline structures.
    
    Args:
        depth (int): Current recursion depth (0 draws base segment)
        size (float): Length of current segment to draw
        total (int): Total segments for color gradient calculation
    """
    global step

    if depth == 0:
        t.pencolor(get_color(step, total))
        step += 1
        t.forward(size)
        return

    ice_fract_2(depth - 1, size / 2, total)
    t.left(120)

    ice_fract_2(depth - 1, size / 4, total)
    t.right(180)

    ice_fract_2(depth - 1, size / 4, total)
    t.left(120)

    ice_fract_2(depth - 1, size / 4, total)
    t.right(180)

    ice_fract_2(depth - 1, size / 4, total)
    t.left(120)
    ice_fract_2(depth - 1, size / 2, total)
