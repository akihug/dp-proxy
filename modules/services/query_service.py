from modules.query_filter.query_filter import filter_query
from modules.query_parser.query_parser import parse_query
from modules.dp_engine.dp_engine import get_noisy_output


def process_query(query: str):
    parsed_query_properties = parse_query(query)
    is_query_allowed = filter_query(parsed_query_properties)
    if is_query_allowed is True:
        return get_noisy_output(query)
    else:
        return None