class EmployeeSalaryCalculate:

    def __init__(self, base_salary: int):
        self.__base_salary = base_salary

    def salary_calculate(self) -> int:
        return int(self.__base_salary * 1.25)
