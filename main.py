class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self._slots = {1: 0, 2: 0, 3: 0}
        self._slots_limits = {1: big, 2: medium, 3: small}

    def addCar(self, carType: int) -> bool:
        if self._slots[carType] == self._slots_limits[carType]:
            return False

        self._slots[carType] += 1
        return True


if __name__ == '__main__':
    a = ParkingSystem(1, 1, 0)
    assert True is a.addCar(1)
    assert True is a.addCar(2)
    assert False is a.addCar(3)
    assert False is a.addCar(1)
