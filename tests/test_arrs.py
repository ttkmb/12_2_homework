import pytest

from utils import arrs


@pytest.fixture
def dictionary():
    return [1, 2, 3]


def test_get():
    assert arrs.get(dictionary, 1, "test") == 2
    with pytest.raises(IndexError):
        assert arrs.get([], 0, "test") == "test"
    with pytest.raises(IndexError):
        assert arrs.get(dictionary, 5) is None
    assert arrs.get(dictionary, -1) is None
    assert arrs.get(['1', 2, [1, 2]], 2) == [1, 2]


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice(dictionary, 1) == [2, 3]
    assert arrs.my_slice(dictionary, -1) == [3]
    assert arrs.my_slice([], 1) == []
    assert arrs.my_slice(dictionary) == [1, 2, 3]
    assert arrs.my_slice(dictionary, end=3) == [1, 2, 3]
    assert arrs.my_slice([], 0, 0) == []
    assert arrs.my_slice([1, 2, 3, 4, 5], -3, -1) == [3, 4]
    assert arrs.my_slice([1, 2, 3, 4, 5], -3, -7) == []
    assert arrs.my_slice([1, 2, 3, 4, 5], 10) == []
    assert arrs.my_slice([1, 2, 3, 4, 5], end=10) == [1, 2, 3, 4, 5]
    assert arrs.my_slice([1, 2, 3, 4, 5], end=-2) == [1, 2, 3]
    assert arrs.my_slice(dictionary, -4) == [1, 2, 3]
