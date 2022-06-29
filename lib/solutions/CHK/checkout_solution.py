

PRICES = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15
}

OFFERS = {
    'A': {'qty': 3, 'price': 130},
    'B': {'qty': 2, 'price': 45},
}


def compute_price(count, full_price, offer):

    if offer:
        offer_qty = offer['qty']
        offer_price = offer['price']
        tot_price = full_price * (count % offer_qty) + offer_price * (count // offer_qty)

    else:
        tot_price = full_price * count

    return tot_price


def checkout(skus: str) -> int:

    items_in_skus = set(skus)

    counts = {item: skus.count(item) for item in items_in_skus}

    tot_checkout = [compute_price(
        count,
        PRICES.get(sku_name, 0),
        OFFERS.get(sku_name, None)
    ) for sku_name, count in counts.items()]

    return tot_checkout






