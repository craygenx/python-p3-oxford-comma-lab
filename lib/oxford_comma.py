def oxford_comma(items):
    if len(items) == 0:
        return ""
    elif len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return f"{items[0]} and {items[1]}"
    else:
        # Join all elements except the last one with commas and add 'and' before the last element
        return f"{', '.join(items[:-1])}, and {items[-1]}"
