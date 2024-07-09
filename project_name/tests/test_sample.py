# Copyright (c) 2018-2023 Yototec

"""
A sample test.
"""

from unittest import TestCase
from pandas import DataFrame  # type: ignore


class TestSample(TestCase):
    """
    A sample test.
    """

    def test_sample(self) -> None:
        """
        Tests.
        """
        df = DataFrame()
        df["value"] = [1, 2, 3]

        self.assertGreater(len(df), 0)
