from django import template

register = template.Library()


@register.filter(name='fcfa')
def fcfa(value):
    """Format a number as Franc CFA with space thousands separator.

    Examples:
    - 1000 -> "1 000 FCFA"
    - 1234.5 -> "1 234.50 FCFA"
    """
    try:
        v = float(value)
    except (TypeError, ValueError):
        return value

    # Use no decimals when value is integer, otherwise two decimals
    if v.is_integer():
        s = f"{int(v):,}".replace(",", " ")
    else:
        s = f"{v:,.2f}".replace(",", " ")

    return f"{s} FCFA"
