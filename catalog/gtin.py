"""Normalizace a seskupování nabídek podle platného EAN/GTIN.

Bez síťových požadavků; připraveno pro budoucí import katalogu.
"""
from collections import defaultdict
import re


def normalize_gtin(value):
    """Vrátí 8/12/13/14místný GTIN s platnou kontrolní číslicí, jinak None."""
    if value is None:
        return None
    raw = str(value).strip().replace(" ", "").replace("-", "")
    if not re.fullmatch(r"\d{8}|\d{12}|\d{13}|\d{14}", raw):
        return None
    total = sum(int(ch) * (3 if i % 2 else 1)
                for i, ch in enumerate(reversed(raw[:-1])))
    check = (10 - total % 10) % 10
    return raw if check == int(raw[-1]) else None


def group_offers_by_gtin(offers):
    """Seskupí nabídky podle GTIN; neplatné/chybějící EAN nepropojuje.

    Každá nabídka je dict s klíčem 'ean' nebo 'gtin'.
    Záměrně neslučuje rozdílné délky GTIN ani neodstraňuje úvodní nuly.
    """
    groups = defaultdict(list)
    unmatched = []
    for offer in offers:
        gtin = normalize_gtin(offer.get("ean") or offer.get("gtin"))
        if gtin:
            groups[gtin].append(offer)
        else:
            unmatched.append(offer)
    return dict(groups), unmatched
