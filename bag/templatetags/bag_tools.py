from decimal import Decimal

from django import template

register = template.Library()


@register.filter(name="calc_subtotal")
def calc_subtotal(price, quantity):
    """
    Multiply a price by a quantity safely and return a Decimal.
    Usage in templates:
        {{ item.product.price|calc_subtotal:item.quantity }}
    """
    try:
        return (Decimal(price) if not isinstance(price, Decimal) else price) * Decimal(quantity)
    except Exception:
        # Fallback to 0 to avoid template crashes
        return Decimal("0.00")
