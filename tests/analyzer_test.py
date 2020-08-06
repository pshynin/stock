import pytest

from analyzer.get_stock_by_volume import get_volume


def test_get_volume():
    assert get_volume('AAPL') is not None
