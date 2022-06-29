

PRICES = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15
}

OFFERS = {
    'A': [{'qty': 3, 'price': 130}, {'qty': 3, 'price': 130}], 
    'B': [{'qty': 2, 'price': 45}],
    'C': [{'qty': 1, 'price': 20}],
    'D': [{'qty': 1, 'price': 15}],
    'E': [{'qty': 1, 'price': 40}]
}

REPLACEMENT_OFFERS = {
    'E': {'qty': 2, 'replace_with': 'B'}
}

def compute_price(count: int, full_price: int, offers: dict) -> int:
    """Compute the price of all the items of a given

    Args:
        count (int): number of items
        full_price (int): full price
        offers (dict): offers definition (qty, price)

    Returns:
        int: total price
    """

    if offers:

            tot_price = 0
            while count > 0:
                for offer in offers:
                    offer_qty = offer['qty']
                    offer_price = offer['price']
                    Noffers = count // offer_qty
                    tot_price, count = tot_price + Noffers * offer_price, - Noffers * offer_qty

        tot_price = full_price * (count % offer_qty) + offer_price * (count // offer_qty)

    else:
        tot_price = full_price * count

    return tot_price


def checkout(skus: str) -> int:
    """Compute the total checkout, accounting for any offers.

    Args:
        skus (str): list of skus in a single-string format.

    Raises:
        TypeError: if skus is not a string.

    Returns:
        int: the total checkout price.
    """
    if not isinstance(skus, str):
        return -1

    items_in_skus = set(skus)

    counts = {item: skus.count(item) for item in items_in_skus}

    # check that all skus exist
    if items_in_skus - set(PRICES):
        # some skus do not exist
        return -1

    tot_checkout = sum([compute_price(
        count,
        PRICES.get(sku_name, 0),
        OFFERS.get(sku_name, None)
    ) for sku_name, count in counts.items()])

    return tot_checkout





