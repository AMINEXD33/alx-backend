#!/usr/bin/env python3
"""module that contains one function to calc pagination"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int):
    """
    The function should return a tuple of size two
    containing a start index and an end index corresponding
    to the range of indexes to return in a list for those particular
    pagination parameters
    """
    start: int = (page - 1) * page_size
    end: int = page * page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        this function returns a chunk of data based onthe pagination params
        passed to it
        """

        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        dataset = self.dataset()
        indexs: List[int, int] = index_range(page=page, page_size=page_size)
        # check bounds
        if indexs[0] > len(dataset):
            # we can't start off bound
            return []
        if indexs[1] > len(dataset):
            # return a list from thta valid start until the
            # max length
            data_list: List = []
            for x in range(indexs[0], len(dataset)):
                data_list.append(dataset[x])
            return data_list
        # both bounds are valid
        data_list: List = []
        for x in range(indexs[0], indexs[1]):
            data_list.append(dataset[x])
        return data_list
