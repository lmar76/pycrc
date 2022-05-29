"""Test the `crc` module."""
import pytest

import crc


@pytest.mark.parametrize(
    'data, expected',
    [
        (b'\x00\x00', b'\x1d\x0f'),
        (b'\x00\x00\x00', b'\xcc\x9c'),
        (b'\xab\xcd\xef\x01', b'\x04\xa2'),
        (b'\x14\x56\xf8\x9a\x00\x01', b'\x7f\xd5')
    ]
)
def test_crc(data, expected):
    """Test the `crc` function."""
    assert crc.crc(data) == expected
