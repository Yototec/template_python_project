# Copyright (c) 2018-2023 Yototec

"""
A sample test.
"""

from pandas import DataFrame  # type: ignore


class TestSample:
    """
    A sample test.
    """

    @staticmethod
    def test_sample() -> None:
        """
        Tests.
        """
        df = DataFrame()
        df["value"] = [1, 2, 3]

        assert len(df) > 0
