import turtle as t


def koch(size: int, depth: int) -> None:
    """
       Draw a Koch curve segment using recursion.

       The Koch curve is a fractal that starts with a straight line and replaces
       the middle third with two segments forming an equilateral triangle.

       Args:
           size (int): Length of the current line segment
           depth (int): Current recursion depth (0 draws straight line)

       Returns:
           None
       """
    if depth == 0:
        t.forward(size)

    else:
        koch(size / 3, depth - 1)
        t.left(60)
        koch(size / 3, depth - 1)
        t.right(120)
        koch(size / 3, depth - 1)
        t.left(60)
        koch(size / 3, depth - 1)


def snowflake(size: int, depth: int) -> None:
    """
       Draw a complete Koch snowflake by combining three Koch curves.

       The Koch snowflake is formed by drawing three Koch curves in a triangular
       pattern, creating a closed fractal shape.

       Args:
           size (int): Length of each side of the snowflake
           depth (int): Recursion depth for the Koch curves

       Returns:
           None
       """
    for _ in range(3):
        koch(size, depth)
        t.right(120)
