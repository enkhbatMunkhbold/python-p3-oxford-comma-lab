def oxford_comma(items):
    # if len(items) == 1:
    #     return items[0]
    # elif len(items) == 2:
    #     return ' and '.join(items)
    # else:
    #     last_item = items.pop()
    #     str = ', '.join(items)
    #     final = ', and '.join([str, last_item])
    #     return final
    if len(items) > 1:
        items[-1] = 'and ' + items[-1]
    
    if len(items) == 2:
        return ' '.join(items)
    else:
        return ', '.join(items)
