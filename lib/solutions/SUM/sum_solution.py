
def _checks(x, y):
    """Internal checks for the compute function.

    Args:
        x (int): input param1
        y (int): input param2

    Raises:
        TypeError: if x or y are not int.
        ValueError: if x or y are larger than 100
    """
    if not isinstance(x, int):
        raise TypeError(f"x must be integer, got {type(x)}")
        
    if not isinstance(y, int):
        raise TypeError(f"y must be integer, got {type(x)}")

    if not 0 <= x <= 100:
        raise ValueError("x must be between 0 and 100 (bounds included), got {x}")

    if not 0 <= y <= 100:
        raise ValueError("y must be between 0 and 100 (bounds included), got {y}")

def compute(x: int, y: int) -> int:

    _checks(x, y)
    
    return x + y
