from configurations.base_config import ALLOWED_AGGS

def filter_query(query_properties: list):
    aggs: list = []
    for item in query_properties[0].select.namedExpressions.seq:
        aggs.append(item.expression.name)
    if all(item in ALLOWED_AGGS for item in aggs):
        return True
    else:
        error = f'Only {",".join(ALLOWED_AGGS)} aggregate queries are allowed!'
        raise ValueError(error)