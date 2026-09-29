import pytest
from fleet import Vehicle

@pytest.fixture
def fueled_vehicle():
    vehicle = Vehicle("AA-12-BB")
    vehicle.refuel(30)
    return vehicle

def test_drive_increases_odometer(fueled_vehicle):
    fueled_vehicle.drive(100)
    assert fueled_vehicle.odometer == 100

def test_drive_uses_fuel(fueled_vehicle):
    fueled_vehicle.drive(100)
    assert fueled_vehicle.fuel == 20

def test_drive_more_than_fuel(fueled_vehicle):
    with pytest.raises(ValueError):
        fueled_vehicle.drive(301)

def test_drive_refuel_above(fueled_vehicle):
    with pytest.raises(ValueError):
        fueled_vehicle.refuel(31)

def test_drive_maxlimit(fueled_vehicle):
    fueled_vehicle.drive(300)
    assert fueled_vehicle.fuel == 0
    assert fueled_vehicle.odometer == 300

def test_refuel_maxlimit(fueled_vehicle):
    fueled_vehicle.refuel(30)
    assert fueled_vehicle.fuel == 60