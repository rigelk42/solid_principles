from abc import ABC, abstractmethod
from enum import Enum


class SpaceShipType(Enum):
    MLF = "Millenium Falcon"
    INF = "UNSC Infinity"
    ENT = "USS Enterprise"
    SER = "Serenity"


class Position:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y


class Size:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height


class Speed:
    def __init__(self, scalar: float, unit: str) -> None:
        self.scalar = scalar
        self.unit = unit


class ShipContext:
    def __init__(self, position: Position, size: Size, speed: Speed) -> None:
        self.position = position
        self.size = size
        self.speed = speed


class Spaceship(ABC):
    def __init__(self, ctx: ShipContext) -> None:
        self.position = ctx.position
        self.size = ctx.size
        self.speed = ctx.speed

    def get_position(self):
        return self.position

    def get_size(self):
        return self.size

    def get_speed(self):
        return self.speed

    @abstractmethod
    def get_info(self) -> str:
        pass


class MilleniumFalcon(Spaceship):
    def get_info(self) -> str:
        return f"""
            Ship Type: Millenium Falcon
            Position: x: {self.get_position().x}, y: {self.get_position().y}
            Size: Width: {self.get_size().width}, Height: {self.get_size().height}
            Speed: {self.get_speed().scalar}/{self.get_speed().unit}
        """


class UNSCInfinity(Spaceship):
    def get_info(self) -> str:
        return f"""
            Ship Type: UNSC Infinity
            Position: x: {self.get_position().x}, y: {self.get_position().y}
            Size: Width: {self.get_size().width}, Height: {self.get_size().height}
            Speed: {self.get_speed().scalar}/{self.get_speed().unit}
        """


class USSEnterprise(Spaceship):
    def get_info(self) -> str:
        return f"""
            Ship Type: USS Enterprise
            Position: x: {self.get_position().x}, y: {self.get_position().y}
            Size: Width: {self.get_size().width}, Height: {self.get_size().height}
            Speed: {self.get_speed().scalar}/{self.get_speed().unit}
        """


class Serenity(Spaceship):
    def get_info(self) -> str:
        return f"""
            Ship Type: Serenity
            Position: x: {self.get_position().x}, y: {self.get_position().y}
            Size: Width: {self.get_size().width}, Height: {self.get_size().height}
            Speed: {self.get_speed().scalar}/{self.get_speed().unit}
        """


class SpaceshipFactory:
    def create_spaceship(
        self, spaceship_type: SpaceShipType, ctx: ShipContext
    ) -> Spaceship:
        if spaceship_type == SpaceShipType.MLF:
            return MilleniumFalcon(ctx)
        elif spaceship_type == SpaceShipType.INF:
            return UNSCInfinity(ctx)
        elif spaceship_type == SpaceShipType.ENT:
            return USSEnterprise(ctx)
        elif spaceship_type == SpaceShipType.SER:
            return Serenity(ctx)
        else:
            raise ValueError(f"{spaceship_type} is not a valid spaceship type.")


if __name__ == "__main__":

    sf = SpaceshipFactory()

    mlf = sf.create_spaceship(
        SpaceShipType.MLF,
        ShipContext(
            Position(10, 20),
            Size(100, 200),
            Speed(1000, "parsecs"),
        ),
    )

    print(mlf.get_info())

    inf = sf.create_spaceship(
        SpaceShipType.INF,
        ShipContext(
            Position(10, 20),
            Size(100, 200),
            Speed(1000, "parsecs"),
        ),
    )

    print(inf.get_info())

    ent = sf.create_spaceship(
        SpaceShipType.ENT,
        ShipContext(
            Position(10, 20),
            Size(100, 200),
            Speed(1000, "parsecs"),
        ),
    )

    print(ent.get_info())

    ser = sf.create_spaceship(
        SpaceShipType.SER,
        ShipContext(
            Position(10, 20),
            Size(100, 200),
            Speed(1000, "parsecs"),
        ),
    )

    print(ser.get_info())
