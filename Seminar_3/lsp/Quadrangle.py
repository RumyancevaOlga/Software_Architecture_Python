from abc import ABC, abstractmethod


class Quadrangle(ABC):
    @abstractmethod
    def area(self) -> int:
        pass
