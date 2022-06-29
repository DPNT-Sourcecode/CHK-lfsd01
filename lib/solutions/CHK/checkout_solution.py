
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
    'K': [{'qty': 2, 'price': 120}, {'qty': 1, 'price': 70}],
    'L': [{'qty': 1, 'price': 90}],
    'M': [{'qty': 1, 'price': 15}],
    'N': [{'qty': 1, 'price': 40}],
    'O': [{'qty': 1, 'price': 10}],
    'P': [{'qty': 5, 'price': 200}, {'qty': 1, 'price': 50}],
    'Q': [{'qty': 3, 'price': 80}, {'qty': 1, 'price': 30}],
    'R': [{'qty': 1, 'price': 50}],
    'S': [{'qty': 1, 'price': 20}],
    'T': [{'qty': 1, 'price': 20}],
    'U': [{'qty': 1, 'price': 40}],
    'V': [{'qty': 3, 'price': 130}, {'qty': 2, 'price': 90}, {'qty': 1, 'price': 50}],
    'W': [{'qty': 1, 'price': 20}],
    'X': [{'qty': 1, 'price': 17}],
    'Y': [{'qty': 1, 'price': 20}],
    'Z': [{'qty': 1, 'price': 21}],
}


REPLACEMENT_OFFERS = {
    'E': {'qty': 2, 'replace_with': 'B', 'replace_qty': 1},
    'F': {'qty': 3, 'replace_with': 'F', 'replace_qty': 1},
    'N': {'qty': 3, 'replace_with': 'M', 'replace_qty': 1},
    'R': {'qty': 3, 'replace_with': 'Q', 'replace_qty': 1},
    'U': {'qty': 4, 'replace_with': 'U', 'replace_qty': 1},
}

MULTI_BUY_OFFERS = [
    {'skus': ['S', 'T', 'X', 'Y', 'Z'], 'qty': 3, 'price': 45}
]


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

    # print(counts)

    # check that all skus exist
    if set(skus) - set(OFFERS):
        # some skus do not exist
        return -1


    # drop zero counts
    counts = {k: v for k, v in counts.items() if v > 0}

    multi_buy_checkout = 0
    # apply multi-buy offers
    for mb_offer in MULTI_BUY_OFFERS:
        # sort skus by decreasing price so it's more convenient for the customer
        sorted_mb_skus = sorted(
            mb_offer['skus'], 
            key=lambda sku: OFFERS[sku][-1]['price'],
            reverse=True
            )

        mb_skus_to_skus = "".join([mb_sku * counts[mb_sku] for mb_sku in sorted_mb_skus if mb_sku in counts])
        print(mb_skus_to_skus)

        # multi_buy_items = {mb_sku: counts[mb_sku] for mb_sku in sorted_mb_skus if mb_sku in counts}
        # Nmulti_buy_items = sum(multi_buy_items.values())
        # print(multi_buy_items)
        # print(Nmulti_buy_items)
        
        # multi_buy_to_be_removed = {mb_sku: 0 for mb_sku in multi_buy_items}
        # while Nmulti_buy_items >= 3:
        #     for mb_sku in sorted_mb_skus:
        #         remove = multi_buy_items[mb_sku]
        #         Nmulti_buy_items -= remove
        #         multi_buy_to_be_removed[mb_sku] += remove

    return 0

    tot_checkout = sum([compute_price(
        count,
        OFFERS.get(sku_name, None)
    ) for sku_name, count in counts.items()])

    return tot_checkout



