import turtle as t


def ice_fract_2(depth: int, size: float) -> None:
    """
    Draw an ice fractal pattern recursively.

    This function generates a fractal pattern that resembles ice crystals
    using recursive line segments with specific angle transformations.

    Args:
        depth (int): Recursion depth. When depth reaches 0, draws a straight line.
        size (float): Length of the current segment to draw.

    Returns:
        None: Function operates by side effects (turtle graphics drawing).
    """
    if depth == 0:
        t.forward(size)

    else:
        ice_fract_2(depth - 1, size // 2)
        t.left(120)
        
        ice_fract_2(depth - 1, size // 4)
        t.right(180)
        
        ice_fract_2(depth - 1, size // 4)
        t.left(120)
        
        ice_fract_2(depth - 1, size // 4)
        t.right(180)
        
        ice_fract_2(depth - 1, size // 4)
        t.left(120)
        
        ice_fract_2(depth - 1, size // 2)
