

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name: str) -> str:
    """Say hello to the world.

    Args:
        friend_name (str): name of the friend to greet.

    Raises:
        TypeError: if friend_name is not str.

    Returns:
        str: the greeting.
    """
    if not isinstance(friend_name, str):
        raise TypeError(
            f"friend_name must be a string, got {type(friend_name)}"
        )

    return f"Hello, World!"


