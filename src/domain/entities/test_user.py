import pytest
import user

def test_should_return_id_and_name_passed_to_constructor() -> None:
    a_user = user.User('1', 'john')

    assert a_user.get_id() == '1'
    assert a_user.get_name() == 'john'

def test_should_raise_error_if_id_is_empty() -> None:
    with pytest.raises(ValueError, match="User id cannot be empty"):
        user.User('', 'john')

def test_should_raise_error_if_name_is_empty() -> None:
    with pytest.raises(ValueError, match="User name cannot be empty"):
        user.User('1', '')