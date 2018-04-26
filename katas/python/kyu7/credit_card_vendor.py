LENGTHS = {
    15: ["AMEX"],
    16: ["Discover", "Mastercard", "VISA"],
    13: ["VISA"]
}

CARD_PREFIX = {
    "34": "AMEX",
    "37": "AMEX",
    "6011": "Discover",
    "51": "Mastercard",
    "52": "Mastercard",
    "53": "Mastercard",
    "54": "Mastercard",
    "55": "Mastercard",
    "4": "VISA"
}


def get_issuer(number):
    return check_prefix_and_length(number)


def _decode_length(number):
    return LENGTHS.get(len(str(number)))


def _decode_prefix(number):
    for prefix, issuer in CARD_PREFIX.items():
        if str(number).startswith(prefix):
            return issuer


def check_prefix_and_length(number):
    vendor = _decode_prefix(number)
    if vendor is None or _decode_length(number) is None:
        return "Unknown"
    return vendor if vendor in _decode_length(number) else "Unknown"
