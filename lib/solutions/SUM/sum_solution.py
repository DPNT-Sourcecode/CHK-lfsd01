
def _checks(x, y):

    if not isinstance(x, int):
        raise TypeError(f"x must be integer, got {type(x)}")
        
    if not isinstance(y, int):
        raise TypeError(f"y must be integer, got {type(x)}")

    if not x < 100:
        raise ValueError("x must be smaller than 100, got {x}")

    if not y < 100:
        raise ValueError("y must be smaller than 100, got {x}")

def compute(x: int, y: int) -> int:

    _checks(x, y)
    
    return x + y


