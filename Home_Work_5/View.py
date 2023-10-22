from Edit3D import Edit3D


class View3D:

    def __init__(self, edit_3D: Edit3D):
        self.__edit_3D = edit_3D

    def get_edit_3D(self):
        return self.__edit_3D

    def set_edit_3D(self, edit_3D: Edit3D):
        self.__edit_3D = edit_3D

    def view(self):
        pass
