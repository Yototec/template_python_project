# Copyright (c) 2018-2025 Yototec Ltd

"""
A sample test.
"""

import unittest
from pandas import DataFrame  # type: ignore


class TestSample(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
