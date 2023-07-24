#!/usr/bin/env python3
"""
function to return a tupleof size two
a start index and an end index 
"""


def index_range(page, page_size) -> tuple:
    # Calculate the start index for the given page and page_size
    start_index = (page - 1) * page_size

    # Calculate the end index for the given page and page_size
    end_index = page * page_size - 1

    return start_index, end_index


if __name__ == "__main__":
    res = index_range(1, 7)
    print(type(res))
    print(res)

    res = index_range(page=3, page_size=15)
    print(type(res))
    print(res)
