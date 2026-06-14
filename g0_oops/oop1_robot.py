# OOP: Encapsulation + Class Variable + __repr__
# Pattern: private state, public interface, class-level data

class Robot:
    DIRECTIONS = ['N', 'E', 'S', 'W']  # class variable — shared, not per-instance

    def __init__(self, x: int = 0, y: int = 0, direction: str = 'N'):
        self._x = x                     # private (convention)
        self._y = y
        self._dir = direction
        self._history = [(x, y)]

    def move(self, steps: int = 1) -> None:
        if self._dir == 'N': self._y += steps
        elif self._dir == 'S': self._y -= steps
        elif self._dir == 'E': self._x += steps
        elif self._dir == 'W': self._x -= steps
        self._history.append((self._x, self._y))

    def turn_right(self) -> None:
        idx = self.DIRECTIONS.index(self._dir)
        self._dir = self.DIRECTIONS[(idx + 1) % 4]

    def turn_left(self) -> None:
        idx = self.DIRECTIONS.index(self._dir)
        self._dir = self.DIRECTIONS[(idx - 1) % 4]

    def position(self) -> tuple:
        return (self._x, self._y)

    def get_history(self) -> list:
        return list(self._history)

    def reset(self) -> None:
        self._x, self._y, self._dir = 0, 0, 'N'
        self._history = [(0, 0)]

    def __repr__(self) -> str:
        return f"Robot(pos={self.position()}, dir={self._dir})"


if __name__ == "__main__":
    r = Robot()
    r.move(3)           # (0, 3)
    r.turn_right()      # now facing E
    r.move(2)           # (2, 3)
    r.turn_left()       # back to N
    print(r)                    # Robot(pos=(2, 3), dir=N)
    print(r.position())         # (2, 3)
    print(r.get_history())      # [(0,0), (0,3), (2,3)]
    r.reset()
    print(r)                    # Robot(pos=(0, 0), dir=N)
