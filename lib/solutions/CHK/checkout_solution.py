

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


def compute_price(sku_name, count, full_price, offer_qty, offer_price):


    # full_price = SKUS_PRICES[sku_name]
    # offer_qty = SKUS_PRICES[sku_name]['qty']
    # offer_price = SKUS_PRICES[sku_name]['price']

    tot_price = full_price * (count % offer_qty) + offer_price * (count // offer_qty)

    return tot_price


def checkout(skus: str) -> int:

    items_in_skus = set(skus)

    counts = {item: skus.count(item) for item in items_in_skus}

    tot_checkout = [compute_price(sku_name, count) for sku_name, count in counts.items()]

    return tot_checkout




