def suggest(product_idea):
    """
    docstring
    """
    if len(product_idea) < 3:
        raise ValueError()
    return product_idea + "inator"
