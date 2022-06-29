
# Note: offers should be sorted by increasing unit price (price/qty value)
OFFERS = {
    'A': [{'qty': 5, 'price': 200}, {'qty': 3, 'price': 130}, {'qty': 1, 'price': 50}],
    'B': [{'qty': 2, 'price': 45}, {'qty': 1, 'price': 30}],
    'C': [{'qty': 1, 'price': 20}],
    'D': [{'qty': 1, 'price': 15}],
    'E': [{'qty': 1, 'price': 40}],
    'F': [{'qty': 1, 'price': 10}],
    'G': [{'qty': 1, 'price': 20}],
    'H': [{'qty': 10, 'price': 80}, {'qty': 5, 'price': 45}, {'qty': 1, 'price': 10}],
    'I': [{'qty': 1, 'price': 35}],
    'J': [{'qty': 1, 'price': 60}],
    'K': [{'qty': 2, 'price': 150}, {'qty': 1, 'price': 80}],
    'L': [{'qty': 1, 'price': 90}],
    'M': [{'qty': 1, 'price': 15}],
    'N': [{'qty': 1, 'price': 40}],
    'O': [{'qty': 1, 'price': 10}],
    'P': [{'qty': 5, 'price': 200}, {'qty': 1, 'price': 50}],
    'Q': [{'qty': 3, 'price': 80}, {'qty': 1, 'price': 30}],
    'R': [{'qty': 1, 'price': 50}],
    'S': [{'qty': 1, 'price': 30}],
    'T': [{'qty': 1, 'price': 20}],
    'U': [{'qty': 1, 'price': 40}],
    'V': [{'qty': 3, 'price': 130}, {'qty': 2, 'price': 90}, {'qty': 1, 'price': 50}],
    'W': [{'qty': 1, 'price': 20}],
    'X': [{'qty': 1, 'price': 90}],
    'Y': [{'qty': 1, 'price': 10}],
    'Z': [{'qty': 1, 'price': 50}],
}


REPLACEMENT_OFFERS = {
    'E': {'qty': 2, 'replace_with': 'B', 'replace_qty': 1},
    'F': {'qty': 3, 'replace_with': 'F', 'replace_qty': 1},
    'N': {'qty': 3, 'replace_with': 'M', 'replace_qty': 1},
    'R': {'qty': 3, 'replace_with': 'Q', 'replace_qty': 1},
    'U': {'qty': 4, 'replace_with': 'U', 'replace_qty': 1},
}


def compute_price(count: int, offers: dict) -> int:
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
        for offer in offers:
            # offers need to be sorted by increasing unit price
            offer_qty = offer['qty']
            offer_price = offer['price']
            Noffers = count // offer_qty
            tot_price += Noffers * offer_price
            count -= Noffers * offer_qty

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

    counts = {item: skus.count(item) for item in OFFERS}

    # apply replacement offers
    for sku, offer in REPLACEMENT_OFFERS.items():
        Noffers = counts[sku] // offer['qty']
        counts[offer['replace_with']] -= Noffers * offer['replace_qty']

    print(counts)

    # check that all skus exist
    if set(skus) - set(OFFERS):
        # some skus do not exist
        return -1

    # drop zero counts
    counts = {k: v for k, v in counts.items() if v > 0}

    tot_checkout = sum([compute_price(
        count,
        OFFERS.get(sku_name, None)
    ) for sku_name, count in counts.items()])

    return tot_checkout
