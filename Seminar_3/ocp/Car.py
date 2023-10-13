from Vehicle import Vehicle


class Car(Vehicle):

    def __init__(self, max_speed: int):
        super().__init__(max_speed, 'Car')

    def calculate_al_lowed_speed(self) -> float:
        return super().calculate_al_lowed_speed() * 0.8
