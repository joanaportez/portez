from app import is_prime


def test_prime_numbers():
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(13) is True
    assert is_prime(17) is True


def test_non_prime_numbers():
    assert is_prime(1) is False
    assert is_prime(0) is False
    assert is_prime(4) is False
    assert is_prime(100) is False
