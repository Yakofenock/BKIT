def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        for item in items:
            if args[0] in item and item[args[0]] is not None:
                yield item[args[0]]

    else:
        for item in items:
            dic = {}
            for value in args:
                if value in item and item[value] is not None:
                    dic[value] = item[value]
            if len(dic) != 0:
                yield dic


goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
]
