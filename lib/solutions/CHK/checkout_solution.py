

SKUS_PRICES = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15
}

SKUS_OFFERS = {
    'A': {'qty': 3, 'price': 130},
    'B': {'qty': 2, 'price': 45},
}

def apply_offers():

    # noinspection PyUnusedLocal
    # skus = unicode string


def checkout(skus: str) -> int:

    items_in_skus = set(skus)

    counts = {item: skus.count(item) for item in items_in_skus}

    tot_checkout = []

    return tot_checkout


