

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name: str) -> str:
    if not isinstance(friend_name, str):
        raise TypeError(
            f"friend_name must be a string, got {type(friend_name)}"
        )

    print(f"Hello, {friend_name}!")
