from snsql.sql.parse import QueryParser


def parse_query(query: str):
    if query.upper().startswith("SELECT"):
        query_properties = QueryParser().queries(query.upper())
        return query_properties
    else:
        raise ValueError("Only SELECT queries are allowed!")