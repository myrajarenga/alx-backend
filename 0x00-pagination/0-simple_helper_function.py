#!/usr/bin/env python3
"""
function to return a tupleof size two
a start index and an end index
"""


def index_range(page, page_size) -> tuple:
    """Calculate the start  and  last index
    for the given page and page_size
    """
    return (((page - 1) * page_size), page * page_size)


if __name__ == "__main__":
    res = index_range(1, 7)
    print(type(res))
    print(res)

    res = index_range(page=3, page_size=15)
    print(type(res))
    print(res)
