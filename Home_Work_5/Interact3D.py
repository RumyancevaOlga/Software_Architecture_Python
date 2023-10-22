from abc import ABC, abstractmethod
from Model3D import Model3D


class Interact3D(ABC):
    @abstractmethod
    def upload_3D(self, model_3d: Model3D):
        pass

    @abstractmethod
    def download_3D(self):
        pass
