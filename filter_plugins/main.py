def map_list(items, sep, headers):
    return [
        dict(zip(headers, list(filter(None, item.split(sep)))))
        for item in items
    ]


def aggregate(items, key, default='_'):
    aggregated = {}
    for item in items:
        aggregated[item.get(key, default)] = item
    return aggregated


class FilterModule:
    def filters(self):
        return {
            'map_list': map_list,
            'aggregate': aggregate
        }
