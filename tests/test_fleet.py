import pytest
from fleet import classify_speed

@pytest.mark.parametrize("speed, expected", [
    (0, "stopped"),
    (1, "normal"),
    (80, "normal"),
    (120, "normal"),
    (121, "speeding"),
    (200, "speeding"),
])
def test_classify_speed(speed, expected):
    assert classify_speed(speed) == expected

@pytest.mark.parametrize("speed", [-1, -5, -100])
def test_negative_speed_raises_error(speed):
    with pytest.raises(ValueError):
        classify_speed(speed)