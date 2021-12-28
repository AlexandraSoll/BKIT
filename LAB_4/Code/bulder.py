from abc import ABC, abstractmethod
from enum import Enum, auto


class BrandType(Enum):
    Apple = auto()
    Xiaomi = auto()
    Samsung = auto()
    Huawei = auto()

class MemoryType(Enum):
    M64 = auto()
    M128 = auto()
    M256 = auto()

class MatrType(Enum):
    IPS = auto()
    Amoled = auto()

class DiagType(Enum):
    D54 = auto()
    D58 = auto()
    D61 = auto()
    D65 = auto()

class Smartphone:
    def __init__(self, name):
        self.name = name
        self.brand = None
        self.memory = None
        self.matr = None
        self.diag = None
        self.cost = None

    def __str__(self):
       info: str = f"Smartphone name: {self.name} \n" \
                   f"{self.brand} \n" \
                   f"{self.memory} \n" \
                   f"{self.matr} \n" \
                   f"{self.diag} \n" \
                   f"Cost: {self.cost} rub"

       return info



class Builder(ABC):

    @abstractmethod
    def add_brand(self) -> None: pass

    @abstractmethod
    def add_memory(self) -> None: pass

    @abstractmethod
    def add_matr(self) -> None: pass

    @abstractmethod
    def add_diag(self) -> None: pass


class Apple11Builder(Builder):

    def __init__(self):
        self.smartphone = Smartphone("Apple 11")
        self.smartphone.cost = 60000

    def add_brand(self) -> None:
        self.smartphone.brand = BrandType.Apple

    def add_memory(self) -> None:
        self.smartphone.memory = MemoryType.M128

    def add_matr(self) -> None:
        self.smartphone.matr = MatrType.IPS

    def add_diag(self) -> None:
        self.smartphone.diag = DiagType.D61

    def get_lap(self) -> Smartphone:
        return self.smartphone


class Huawei50LiteBuilder(Builder):

    def __init__(self):
        self.smartphone = Smartphone("Huawei 50 Lite")
        self.smartphone.cost = 25000

    def add_brand(self) -> None:
        self.smartphone.brand = BrandType.Huawei

    def add_memory(self) -> None:
        self.smartphone.memory = MemoryType.M256

    def add_matr(self) -> None:
        self.smartphone.matr = MatrType.Amoled

    def add_diag(self) -> None:
        self.smartphone.diag = DiagType.D65

    def get_lap(self) -> Smartphone:
        return self.smartphone


class Director:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder: Builder):
        self.builder = builder

    def make_lap(self):
        if not self.builder:
            raise ValueError("Builder didn't set")
        self.builder.add_brand()
        self.builder.add_memory()
        self.builder.add_matr()
        self.builder.add_diag()


def check_cost(name1):
    for it1 in (Apple11Builder, Huawei50LiteBuilder):
        director1 = Director()
        builder1 = it1()
        director1.set_builder(builder1)
        director1.make_lap()
        smartphone1 = builder1.get_lap()
        if smartphone1.name == name1:
            return smartphone1.cost

def sum_cost(x):
    for it1 in (Apple11Builder, Huawei50LiteBuilder):
        director1 = Director()
        builder1 = it1()
        director1.set_builder(builder1)
        director1.make_lap()
        smartphone1 = builder1.get_lap()
        x = x + smartphone1.cost
    return x


if __name__ == "__main__":
    print("Объекты:")
    director = Director()
    for it in (Apple11Builder, Huawei50LiteBuilder):
        builder = it()
        director.set_builder(builder)
        director.make_lap()
        smartphone = builder.get_lap()
        print(smartphone)
        print('---------------')
    name = "Huawei 50 Lite"
    print(name, "Cost:", check_cost(name))
    x = 0
    print('sum = ', sum_cost(x))
