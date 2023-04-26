from utils import dicts


def test_get_val():
    assert dicts.get_val({"abc": "123"}, "abc") == "123"
    assert dicts.get_val({}, "abc", ) == 'git'
    assert dicts.get_val({"abc": "123"}, "def", "test") == "test"
